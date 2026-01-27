"""
NITARA VLC Simulator - Windows GUI
Simulates WM (Weighing Machine) and MA (Milk Analyzer) devices
Connect USB-to-UART adapters to test with real connector hardware
"""

import sys
import random
import threading
import time
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGroupBox, QLabel, QComboBox, QPushButton, QTextEdit, QGridLayout,
    QSpinBox, QCheckBox, QFrame, QSplitter, QMessageBox
)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QObject
from PyQt5.QtGui import QFont, QColor, QPalette

import serial
import serial.tools.list_ports

from sample_data import (
    WM_MODELS, MA_MODELS, WM_SAMPLES, MA_SAMPLES,
    WM_CODE_0000, MA_CODE_0000, BAUD_RATES, get_ma_mode,
    MA_MODE_TIMEOUT, MA_MODE_PARENTHESES, MA_MODE_NEWLINE
)


class SerialSignals(QObject):
    """Signals for thread-safe GUI updates"""
    log_message = pyqtSignal(str)
    tx_count_update = pyqtSignal(str, int)  # device, count


class VLCSimulator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NC Simulator v1.1")
        self.setMinimumSize(1000, 700)

        # Serial ports
        self.wm_serial = None
        self.ma_serial = None

        # State
        self.wm_continuous = False
        self.ma_continuous = False
        self.wm_sample_index = 0
        self.ma_sample_index = 0
        self.wm_tx_count = 0
        self.ma_tx_count = 0
        self.last_wm_data = None
        self.last_ma_data = None

        # Auto Test state
        self.auto_test_running = False
        self.auto_test_cycle = 0
        self.auto_test_wm_count = 0
        self.auto_test_wm_target = 20  # Send 20 WM data per cycle
        self.auto_test_cycle_time = 60000  # 1 minute in ms

        # Signals for thread-safe updates
        self.signals = SerialSignals()
        self.signals.log_message.connect(self.append_log)
        self.signals.tx_count_update.connect(self.update_tx_count)

        # Timers
        self.wm_timer = QTimer()
        self.wm_timer.timeout.connect(self.send_wm_data)
        self.ma_timer = QTimer()
        self.ma_timer.timeout.connect(self.send_ma_data)

        # Auto Test timers
        self.auto_test_wm_timer = QTimer()
        self.auto_test_wm_timer.timeout.connect(self.auto_test_send_wm)
        self.auto_test_cycle_timer = QTimer()
        self.auto_test_cycle_timer.timeout.connect(self.auto_test_new_cycle)

        self.init_ui()
        self.refresh_ports()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # Left panel - Configuration
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        # COM Port Selection
        port_group = QGroupBox("COM Port Selection")
        port_layout = QGridLayout()

        port_layout.addWidget(QLabel("WM Port:"), 0, 0)
        self.wm_port_combo = QComboBox()
        port_layout.addWidget(self.wm_port_combo, 0, 1)

        port_layout.addWidget(QLabel("MA Port:"), 1, 0)
        self.ma_port_combo = QComboBox()
        port_layout.addWidget(self.ma_port_combo, 1, 1)

        refresh_btn = QPushButton("Refresh Ports")
        refresh_btn.clicked.connect(self.refresh_ports)
        port_layout.addWidget(refresh_btn, 2, 0, 1, 2)

        port_group.setLayout(port_layout)
        left_layout.addWidget(port_group)

        # WM Configuration
        wm_group = QGroupBox("WM (Weighing Machine)")
        wm_layout = QGridLayout()

        wm_layout.addWidget(QLabel("Model:"), 0, 0)
        self.wm_model_combo = QComboBox()
        for model, name in WM_MODELS.items():
            self.wm_model_combo.addItem(f"{model} - {name}", model)
        wm_layout.addWidget(self.wm_model_combo, 0, 1)

        wm_layout.addWidget(QLabel("Baud Rate:"), 1, 0)
        self.wm_baud_combo = QComboBox()
        for baud in BAUD_RATES:
            self.wm_baud_combo.addItem(str(baud), baud)
        self.wm_baud_combo.setCurrentText("9600")
        wm_layout.addWidget(self.wm_baud_combo, 1, 1)

        wm_layout.addWidget(QLabel("End Char:"), 2, 0)
        self.wm_end_combo = QComboBox()
        self.wm_end_combo.addItem("\\n (Newline)", "\n")
        self.wm_end_combo.addItem("\\r (CR)", "\r")
        self.wm_end_combo.addItem("\\r\\n (CRLF)", "\r\n")
        self.wm_end_combo.addItem("None", "")
        wm_layout.addWidget(self.wm_end_combo, 2, 1)

        self.wm_connect_btn = QPushButton("Connect WM")
        self.wm_connect_btn.clicked.connect(self.toggle_wm_connection)
        wm_layout.addWidget(self.wm_connect_btn, 3, 0, 1, 2)

        self.wm_status_label = QLabel("Status: Disconnected")
        self.wm_status_label.setStyleSheet("color: red;")
        wm_layout.addWidget(self.wm_status_label, 4, 0, 1, 2)

        self.wm_tx_label = QLabel("TX Count: 0")
        wm_layout.addWidget(self.wm_tx_label, 5, 0, 1, 2)

        wm_group.setLayout(wm_layout)
        left_layout.addWidget(wm_group)

        # MA Configuration
        ma_group = QGroupBox("MA (Milk Analyzer)")
        ma_layout = QGridLayout()

        ma_layout.addWidget(QLabel("Model:"), 0, 0)
        self.ma_model_combo = QComboBox()
        for model, name in MA_MODELS.items():
            self.ma_model_combo.addItem(f"{model} - {name}", model)
        self.ma_model_combo.currentIndexChanged.connect(self.on_ma_model_changed)
        ma_layout.addWidget(self.ma_model_combo, 0, 1)

        ma_layout.addWidget(QLabel("Baud Rate:"), 1, 0)
        self.ma_baud_combo = QComboBox()
        for baud in BAUD_RATES:
            self.ma_baud_combo.addItem(str(baud), baud)
        self.ma_baud_combo.setCurrentText("9600")
        ma_layout.addWidget(self.ma_baud_combo, 1, 1)

        self.ma_mode_label = QLabel("Mode: TIMEOUT")
        ma_layout.addWidget(self.ma_mode_label, 2, 0, 1, 2)

        self.ma_connect_btn = QPushButton("Connect MA")
        self.ma_connect_btn.clicked.connect(self.toggle_ma_connection)
        ma_layout.addWidget(self.ma_connect_btn, 3, 0, 1, 2)

        self.ma_status_label = QLabel("Status: Disconnected")
        self.ma_status_label.setStyleSheet("color: red;")
        ma_layout.addWidget(self.ma_status_label, 4, 0, 1, 2)

        self.ma_tx_label = QLabel("TX Count: 0")
        ma_layout.addWidget(self.ma_tx_label, 5, 0, 1, 2)

        ma_group.setLayout(ma_layout)
        left_layout.addWidget(ma_group)

        # Control Buttons
        ctrl_group = QGroupBox("Controls")
        ctrl_layout = QGridLayout()

        # WM Controls
        ctrl_layout.addWidget(QLabel("WM:"), 0, 0)

        wm_send_btn = QPushButton("Send Normal")
        wm_send_btn.clicked.connect(self.start_wm_normal)
        wm_send_btn.setStyleSheet("background-color: #4CAF50; color: white;")
        ctrl_layout.addWidget(wm_send_btn, 0, 1)

        wm_0000_btn = QPushButton("Code 0000")
        wm_0000_btn.clicked.connect(self.start_wm_0000)
        wm_0000_btn.setStyleSheet("background-color: #2196F3; color: white;")
        ctrl_layout.addWidget(wm_0000_btn, 0, 2)

        wm_stop_btn = QPushButton("Stop")
        wm_stop_btn.clicked.connect(self.stop_wm)
        wm_stop_btn.setStyleSheet("background-color: #f44336; color: white;")
        ctrl_layout.addWidget(wm_stop_btn, 0, 3)

        # MA Controls
        ctrl_layout.addWidget(QLabel("MA:"), 1, 0)

        ma_send_btn = QPushButton("Send Normal")
        ma_send_btn.clicked.connect(self.start_ma_normal)
        ma_send_btn.setStyleSheet("background-color: #4CAF50; color: white;")
        ctrl_layout.addWidget(ma_send_btn, 1, 1)

        ma_0000_btn = QPushButton("Code 0000")
        ma_0000_btn.clicked.connect(self.start_ma_0000)
        ma_0000_btn.setStyleSheet("background-color: #2196F3; color: white;")
        ctrl_layout.addWidget(ma_0000_btn, 1, 2)

        ma_stop_btn = QPushButton("Stop")
        ma_stop_btn.clicked.connect(self.stop_ma)
        ma_stop_btn.setStyleSheet("background-color: #f44336; color: white;")
        ctrl_layout.addWidget(ma_stop_btn, 1, 3)

        # BOTH Controls (like Pico2W buttons)
        ctrl_layout.addWidget(QLabel("BOTH:"), 2, 0)

        both_send_btn = QPushButton("Send Normal")
        both_send_btn.clicked.connect(self.start_both_normal)
        both_send_btn.setStyleSheet("background-color: #9C27B0; color: white; font-weight: bold;")
        ctrl_layout.addWidget(both_send_btn, 2, 1)

        both_0000_btn = QPushButton("Code 0000")
        both_0000_btn.clicked.connect(self.start_both_0000)
        both_0000_btn.setStyleSheet("background-color: #FF9800; color: white; font-weight: bold;")
        ctrl_layout.addWidget(both_0000_btn, 2, 2)

        both_stop_btn = QPushButton("Stop All")
        both_stop_btn.clicked.connect(self.stop_both)
        both_stop_btn.setStyleSheet("background-color: #E91E63; color: white; font-weight: bold;")
        ctrl_layout.addWidget(both_stop_btn, 2, 3)

        ctrl_group.setLayout(ctrl_layout)
        left_layout.addWidget(ctrl_group)

        # Auto Test Section
        auto_group = QGroupBox("Auto Test (1 MA + 20 WM per minute)")
        auto_layout = QGridLayout()

        self.auto_start_btn = QPushButton("START Auto Test")
        self.auto_start_btn.clicked.connect(self.start_auto_test)
        self.auto_start_btn.setStyleSheet("background-color: #00BCD4; color: white; font-weight: bold; padding: 10px;")
        auto_layout.addWidget(self.auto_start_btn, 0, 0)

        self.auto_stop_btn = QPushButton("STOP Auto Test")
        self.auto_stop_btn.clicked.connect(self.stop_auto_test)
        self.auto_stop_btn.setStyleSheet("background-color: #f44336; color: white; font-weight: bold; padding: 10px;")
        self.auto_stop_btn.setEnabled(False)
        auto_layout.addWidget(self.auto_stop_btn, 0, 1)

        self.auto_status_label = QLabel("Status: Idle")
        self.auto_status_label.setStyleSheet("font-weight: bold; color: #888;")
        auto_layout.addWidget(self.auto_status_label, 1, 0, 1, 2)

        self.auto_cycle_label = QLabel("Cycle: 0 | WM: 0/20 | MA: 0")
        auto_layout.addWidget(self.auto_cycle_label, 2, 0, 1, 2)

        auto_group.setLayout(auto_layout)
        left_layout.addWidget(auto_group)

        left_layout.addStretch()

        # Right panel - Log
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)

        log_group = QGroupBox("Log Output")
        log_layout = QVBoxLayout()

        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setFont(QFont("Consolas", 9))
        self.log_text.setStyleSheet("background-color: #1e1e1e; color: #00ff00;")
        log_layout.addWidget(self.log_text)

        clear_btn = QPushButton("Clear Log")
        clear_btn.clicked.connect(self.log_text.clear)
        log_layout.addWidget(clear_btn)

        log_group.setLayout(log_layout)
        right_layout.addWidget(log_group)

        # Add panels to main layout
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([400, 600])
        main_layout.addWidget(splitter)

        self.append_log("=== NC Simulator v1.1 ===")
        self.append_log("Connect USB-to-UART adapters to WM and MA ports")
        self.append_log("Then connect to Connector for testing")
        self.append_log("")

    def refresh_ports(self):
        """Refresh available COM ports"""
        ports = serial.tools.list_ports.comports()

        current_wm = self.wm_port_combo.currentText()
        current_ma = self.ma_port_combo.currentText()

        self.wm_port_combo.clear()
        self.ma_port_combo.clear()

        for port in ports:
            self.wm_port_combo.addItem(f"{port.device} - {port.description}", port.device)
            self.ma_port_combo.addItem(f"{port.device} - {port.description}", port.device)

        # Restore selection if available
        for i in range(self.wm_port_combo.count()):
            if current_wm and current_wm.startswith(self.wm_port_combo.itemData(i)):
                self.wm_port_combo.setCurrentIndex(i)
                break
        for i in range(self.ma_port_combo.count()):
            if current_ma and current_ma.startswith(self.ma_port_combo.itemData(i)):
                self.ma_port_combo.setCurrentIndex(i)
                break

        self.append_log(f"Found {len(ports)} COM ports")

    def on_ma_model_changed(self):
        """Update MA mode label when model changes"""
        model = self.ma_model_combo.currentData()
        if model:
            mode = get_ma_mode(model)
            self.ma_mode_label.setText(f"Mode: {mode}")

    def toggle_wm_connection(self):
        """Connect/disconnect WM serial port"""
        if self.wm_serial and self.wm_serial.is_open:
            self.wm_serial.close()
            self.wm_serial = None
            self.wm_connect_btn.setText("Connect WM")
            self.wm_status_label.setText("Status: Disconnected")
            self.wm_status_label.setStyleSheet("color: red;")
            self.append_log("[WM] Disconnected")
        else:
            try:
                port = self.wm_port_combo.currentData()
                baud = self.wm_baud_combo.currentData()
                self.wm_serial = serial.Serial(port, baud, timeout=0.1)
                self.wm_connect_btn.setText("Disconnect WM")
                self.wm_status_label.setText(f"Status: Connected ({port} @ {baud})")
                self.wm_status_label.setStyleSheet("color: green;")
                self.append_log(f"[WM] Connected: {port} @ {baud} baud")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to connect WM: {e}")
                self.append_log(f"[WM] Connection error: {e}")

    def toggle_ma_connection(self):
        """Connect/disconnect MA serial port"""
        if self.ma_serial and self.ma_serial.is_open:
            self.ma_serial.close()
            self.ma_serial = None
            self.ma_connect_btn.setText("Connect MA")
            self.ma_status_label.setText("Status: Disconnected")
            self.ma_status_label.setStyleSheet("color: red;")
            self.append_log("[MA] Disconnected")
        else:
            try:
                port = self.ma_port_combo.currentData()
                baud = self.ma_baud_combo.currentData()
                self.ma_serial = serial.Serial(port, baud, timeout=0.1)
                self.ma_connect_btn.setText("Disconnect MA")
                self.ma_status_label.setText(f"Status: Connected ({port} @ {baud})")
                self.ma_status_label.setStyleSheet("color: green;")
                self.append_log(f"[MA] Connected: {port} @ {baud} baud")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to connect MA: {e}")
                self.append_log(f"[MA] Connection error: {e}")

    def get_wm_sample(self, code_0000=False):
        """Get WM sample data"""
        model = self.wm_model_combo.currentData()
        if code_0000:
            return WM_CODE_0000.get(model, "+0000.00Kg")
        else:
            samples = WM_SAMPLES.get(model, WM_SAMPLES[9001])
            self.wm_sample_index = (self.wm_sample_index + 1) % len(samples)
            return samples[self.wm_sample_index]

    def get_ma_sample(self, code_0000=False):
        """Get MA sample data"""
        model = self.ma_model_combo.currentData()
        if code_0000:
            return MA_CODE_0000.get(model, MA_CODE_0000[1001])
        else:
            samples = MA_SAMPLES.get(model, MA_SAMPLES[1001])
            self.ma_sample_index = (self.ma_sample_index + 1) % len(samples)
            return samples[self.ma_sample_index]

    def send_wm_data(self):
        """Send WM data via serial"""
        if not self.wm_continuous:
            return

        self.wm_tx_count += 1
        self.wm_tx_label.setText(f"TX Count: {self.wm_tx_count}")

        # Try to send via serial if connected
        if self.wm_serial and self.wm_serial.is_open:
            try:
                end_char = self.wm_end_combo.currentData()
                data = self.last_wm_data + end_char
                self.wm_serial.write(data.encode())
                self.append_log(f"[WM TX#{self.wm_tx_count}] {repr(self.last_wm_data)}")
            except Exception as e:
                self.append_log(f"[WM TX#{self.wm_tx_count}] {repr(self.last_wm_data)} (Serial Error: {e})")
        else:
            self.append_log(f"[WM TX#{self.wm_tx_count}] {repr(self.last_wm_data)} (No Port)")

    def send_ma_data(self):
        """Send MA data via serial"""
        if not self.ma_continuous:
            return

        self.ma_tx_count += 1
        self.ma_tx_label.setText(f"TX Count: {self.ma_tx_count}")

        # Try to send via serial if connected
        if self.ma_serial and self.ma_serial.is_open:
            try:
                self.ma_serial.write(self.last_ma_data.encode())
                self.append_log(f"[MA TX#{self.ma_tx_count}]")
                self.append_log(f"{self.last_ma_data}")
                self.append_log("")
            except Exception as e:
                self.append_log(f"[MA TX#{self.ma_tx_count}] (Serial Error: {e})")
                self.append_log(f"{self.last_ma_data}")
                self.append_log("")
        else:
            self.append_log(f"[MA TX#{self.ma_tx_count}] (No Port)")
            self.append_log(f"{self.last_ma_data}")
            self.append_log("")

    def start_wm_normal(self):
        """Start WM continuous transmission with normal data"""
        self.last_wm_data = self.get_wm_sample(code_0000=False)
        self.wm_continuous = True
        self.wm_timer.start(100)  # Match Pico VLC timing (~10 Hz)
        connected = "(Connected)" if self.wm_serial and self.wm_serial.is_open else "(No Port)"
        self.append_log(f"[WM] Started continuous: {self.last_wm_data} {connected}")

    def start_wm_0000(self):
        """Start WM continuous transmission with code 0000 data"""
        self.last_wm_data = self.get_wm_sample(code_0000=True)
        self.wm_continuous = True
        self.wm_timer.start(100)  # Match Pico VLC timing
        connected = "(Connected)" if self.wm_serial and self.wm_serial.is_open else "(No Port)"
        self.append_log(f"[WM] Started Code 0000: {self.last_wm_data} {connected}")

    def stop_wm(self):
        """Stop WM transmission"""
        self.wm_continuous = False
        self.wm_timer.stop()
        self.append_log("[WM] Stopped")

    def start_ma_normal(self):
        """Start MA transmission with normal data"""
        model = self.ma_model_combo.currentData()
        mode = get_ma_mode(model)
        self.last_ma_data = self.get_ma_sample(code_0000=False)
        connected = "(Connected)" if self.ma_serial and self.ma_serial.is_open else "(No Port)"

        if mode == MA_MODE_TIMEOUT:
            # Single-shot for timeout mode
            self.ma_tx_count += 1
            self.ma_tx_label.setText(f"TX Count: {self.ma_tx_count}")

            if self.ma_serial and self.ma_serial.is_open:
                try:
                    self.ma_serial.write(self.last_ma_data.encode())
                    self.append_log(f"[MA TX#{self.ma_tx_count}] Single-shot:")
                except Exception as e:
                    self.append_log(f"[MA TX#{self.ma_tx_count}] Single-shot (Error: {e}):")
            else:
                self.append_log(f"[MA TX#{self.ma_tx_count}] Single-shot (No Port):")
            self.append_log(f"{self.last_ma_data}")
            self.append_log("")
        else:
            # Continuous for PARENTHESES and NEWLINE modes
            self.ma_continuous = True
            self.ma_timer.start(100)  # Match Pico VLC timing
            self.append_log(f"[MA] Started continuous ({mode}) {connected}")

    def start_ma_0000(self):
        """Start MA transmission with code 0000 data"""
        model = self.ma_model_combo.currentData()
        mode = get_ma_mode(model)
        self.last_ma_data = self.get_ma_sample(code_0000=True)
        connected = "(Connected)" if self.ma_serial and self.ma_serial.is_open else "(No Port)"

        if mode == MA_MODE_TIMEOUT:
            # Single-shot
            self.ma_tx_count += 1
            self.ma_tx_label.setText(f"TX Count: {self.ma_tx_count}")

            if self.ma_serial and self.ma_serial.is_open:
                try:
                    self.ma_serial.write(self.last_ma_data.encode())
                    self.append_log(f"[MA TX#{self.ma_tx_count}] Code 0000 single-shot:")
                except Exception as e:
                    self.append_log(f"[MA TX#{self.ma_tx_count}] Code 0000 single-shot (Error: {e}):")
            else:
                self.append_log(f"[MA TX#{self.ma_tx_count}] Code 0000 single-shot (No Port):")
            self.append_log(f"{self.last_ma_data}")
            self.append_log("")
        else:
            # Continuous
            self.ma_continuous = True
            self.ma_timer.start(100)  # Match Pico VLC timing
            self.append_log(f"[MA] Started Code 0000 continuous ({mode}) {connected}")

    def stop_ma(self):
        """Stop MA transmission"""
        self.ma_continuous = False
        self.ma_timer.stop()
        self.append_log("[MA] Stopped")

    def start_both_normal(self):
        """Start both WM and MA with normal data (like Pico2W BUTTON_A)"""
        self.append_log("=== BOTH: Starting WM + MA normal ===")
        self.start_wm_normal()
        self.start_ma_normal()

    def start_both_0000(self):
        """Start both WM and MA with code 0000 (like Pico2W BUTTON_B)"""
        self.append_log("=== BOTH: Starting WM + MA Code 0000 ===")
        self.start_wm_0000()
        self.start_ma_0000()

    def stop_both(self):
        """Stop both WM and MA"""
        self.stop_wm()
        self.stop_ma()
        self.append_log("=== BOTH STOPPED ===")

    def append_log(self, message):
        """Append message to log"""
        timestamp = time.strftime("%H:%M:%S")
        self.log_text.append(f"[{timestamp}] {message}")
        # Auto-scroll to bottom
        scrollbar = self.log_text.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def update_tx_count(self, device, count):
        """Update TX count label"""
        if device == "wm":
            self.wm_tx_label.setText(f"TX Count: {count}")
        else:
            self.ma_tx_label.setText(f"TX Count: {count}")

    # ==================== AUTO TEST FUNCTIONS ====================

    def start_auto_test(self):
        """Start the automated test cycle"""
        self.auto_test_running = True
        self.auto_test_cycle = 0
        self.auto_test_wm_count = 0

        # Update UI
        self.auto_start_btn.setEnabled(False)
        self.auto_stop_btn.setEnabled(True)
        self.auto_status_label.setText("Status: Running")
        self.auto_status_label.setStyleSheet("font-weight: bold; color: #00BCD4;")

        self.append_log("=== AUTO TEST STARTED ===")
        self.append_log("Cycle: 1 MA + 20 WM data, repeating every 1 minute")

        # Start first cycle
        self.auto_test_new_cycle()

    def stop_auto_test(self):
        """Stop the automated test"""
        self.auto_test_running = False
        self.auto_test_wm_timer.stop()
        self.auto_test_cycle_timer.stop()

        # Update UI
        self.auto_start_btn.setEnabled(True)
        self.auto_stop_btn.setEnabled(False)
        self.auto_status_label.setText("Status: Stopped")
        self.auto_status_label.setStyleSheet("font-weight: bold; color: #f44336;")

        self.append_log("=== AUTO TEST STOPPED ===")
        self.append_log(f"Total cycles completed: {self.auto_test_cycle}")

    def auto_test_new_cycle(self):
        """Start a new auto test cycle"""
        if not self.auto_test_running:
            return

        self.auto_test_cycle += 1
        self.auto_test_wm_count = 0

        self.append_log(f"--- Cycle #{self.auto_test_cycle} Started ---")

        # Step 1: Send 1 MA data
        self.auto_test_send_ma()

        # Step 2: Start sending WM data
        self.auto_test_wm_timer.start(100)  # Send WM every 100ms

        # Step 3: Schedule next cycle in 1 minute
        self.auto_test_cycle_timer.start(self.auto_test_cycle_time)

        self.update_auto_test_labels()

    def auto_test_send_ma(self):
        """Send single MA data for auto test"""
        self.last_ma_data = self.get_ma_sample(code_0000=False)
        self.ma_tx_count += 1
        self.ma_tx_label.setText(f"TX Count: {self.ma_tx_count}")

        if self.ma_serial and self.ma_serial.is_open:
            try:
                self.ma_serial.write(self.last_ma_data.encode())
                self.append_log(f"[AUTO-MA #{self.ma_tx_count}] Sent")
            except Exception as e:
                self.append_log(f"[AUTO-MA #{self.ma_tx_count}] Error: {e}")
        else:
            self.append_log(f"[AUTO-MA #{self.ma_tx_count}] (No Port)")

    def auto_test_send_wm(self):
        """Send WM data for auto test"""
        if not self.auto_test_running:
            self.auto_test_wm_timer.stop()
            return

        # Check if we've sent 20 WM data
        if self.auto_test_wm_count >= self.auto_test_wm_target:
            self.auto_test_wm_timer.stop()
            self.auto_status_label.setText(f"Status: Waiting for next cycle...")
            self.append_log(f"[AUTO] WM complete (20/20), waiting for next cycle...")
            return

        self.auto_test_wm_count += 1
        self.last_wm_data = self.get_wm_sample(code_0000=False)
        self.wm_tx_count += 1
        self.wm_tx_label.setText(f"TX Count: {self.wm_tx_count}")

        if self.wm_serial and self.wm_serial.is_open:
            try:
                end_char = self.wm_end_combo.currentData()
                data = self.last_wm_data + end_char
                self.wm_serial.write(data.encode())
                self.append_log(f"[AUTO-WM #{self.auto_test_wm_count}/20] {repr(self.last_wm_data)}")
            except Exception as e:
                self.append_log(f"[AUTO-WM #{self.auto_test_wm_count}/20] Error: {e}")
        else:
            self.append_log(f"[AUTO-WM #{self.auto_test_wm_count}/20] {repr(self.last_wm_data)} (No Port)")

        self.update_auto_test_labels()

    def update_auto_test_labels(self):
        """Update auto test status labels"""
        self.auto_cycle_label.setText(
            f"Cycle: {self.auto_test_cycle} | WM: {self.auto_test_wm_count}/{self.auto_test_wm_target} | MA: {self.auto_test_cycle}"
        )
        if self.auto_test_wm_count < self.auto_test_wm_target:
            self.auto_status_label.setText(f"Status: Sending WM ({self.auto_test_wm_count}/{self.auto_test_wm_target})")

    def closeEvent(self, event):
        """Clean up on close"""
        self.stop_both()
        self.auto_test_running = False
        self.auto_test_wm_timer.stop()
        self.auto_test_cycle_timer.stop()
        if self.wm_serial and self.wm_serial.is_open:
            self.wm_serial.close()
        if self.ma_serial and self.ma_serial.is_open:
            self.ma_serial.close()
        event.accept()


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # Dark theme
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    window = VLCSimulator()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
