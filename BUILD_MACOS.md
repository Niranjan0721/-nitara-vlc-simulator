# NC Simulator - macOS Build Instructions

## Prerequisites

1. **macOS 10.13 (High Sierra) or later**
2. **Python 3.8+** - Install from https://www.python.org/downloads/ or via Homebrew:
   ```bash
   brew install python3
   ```

## Files for macOS

Copy these files to your Mac:
- `main.py` - Main application
- `sample_data.py` - Sample data definitions
- `requirements.txt` - Python dependencies
- `install_macos.sh` - Dependency installer
- `run_macos.sh` - Run script (development)
- `build_macos.sh` - Simple build script
- `build_macos_app.sh` - Full .app bundle build script
- `NC_Simulator_macos.spec` - PyInstaller spec file

## Quick Start

### Step 1: Make scripts executable
```bash
chmod +x *.sh
```

### Step 2: Install dependencies
```bash
./install_macos.sh
```

### Step 3: Test the application
```bash
./run_macos.sh
```

### Step 4: Build the .app bundle
```bash
./build_macos_app.sh
```

## Output

After building, you'll find:
- `dist/NC_Simulator.app` - The macOS application bundle

## Installation

Copy to Applications folder:
```bash
sudo cp -r dist/NC_Simulator.app /Applications/
```

## Creating a DMG for Distribution

```bash
hdiutil create -volname "NC Simulator" -srcfolder dist/NC_Simulator.app -ov NC_Simulator.dmg
```

## Serial Port Notes

On macOS, serial ports appear as:
- `/dev/tty.usbserial-*` - USB-to-Serial adapters
- `/dev/tty.usbmodem*` - USB modems
- `/dev/cu.usbserial-*` - Call-up devices (use these for output)

The application will automatically detect available ports.

## Troubleshooting

### "App is damaged" error
Run this command to remove quarantine attribute:
```bash
xattr -cr /Applications/NC_Simulator.app
```

### Permission denied on serial port
Add your user to the dialout group or run:
```bash
sudo chmod 666 /dev/tty.usbserial-*
```

### PyQt5 installation issues on Apple Silicon (M1/M2/M3)
```bash
pip3 install --upgrade pip
pip3 install PyQt5 --config-settings --confirm-license= --verbose
```

## Building for Both Intel and Apple Silicon

To build a universal binary (works on both Intel and Apple Silicon Macs):
```bash
pyinstaller --target-arch universal2 NC_Simulator_macos.spec
```

Note: This requires building on macOS 11+ with Xcode installed.
