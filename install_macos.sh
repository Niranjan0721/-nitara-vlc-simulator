#!/bin/bash
echo "=== NC Simulator - Installing Dependencies for macOS ==="
echo ""

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 is not installed!"
    echo ""
    echo "Install Python3 using one of these methods:"
    echo "  1. Download from: https://www.python.org/downloads/"
    echo "  2. Using Homebrew: brew install python3"
    exit 1
fi

echo "Python3 found: $(python3 --version)"
echo ""

# Check if pip3 is available
if ! command -v pip3 &> /dev/null; then
    echo "Installing pip..."
    python3 -m ensurepip --upgrade
fi

echo "Installing Python dependencies..."
pip3 install --user PyQt5>=5.15.0 pyserial>=3.5 pyinstaller>=6.0.0

echo ""
echo "============================================"
echo "INSTALLATION COMPLETE!"
echo "============================================"
echo ""
echo "You can now run the simulator:"
echo "  ./run_macos.sh"
echo ""
echo "Or build the .app bundle:"
echo "  ./build_macos.sh"
echo ""
