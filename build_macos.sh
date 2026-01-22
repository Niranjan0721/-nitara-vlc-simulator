#!/bin/bash
echo "=== NC Simulator - Building macOS App ==="
echo ""

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 is not installed!"
    echo "Please install Python3 from https://www.python.org/downloads/"
    exit 1
fi

# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt

echo ""
echo "Building macOS application..."
echo ""

# Build macOS app bundle
pyinstaller --onefile \
    --windowed \
    --name "NC_Simulator" \
    --osx-bundle-identifier "com.nitara.vlcsimulator" \
    main.py

echo ""
echo "============================================"
echo "BUILD COMPLETE!"
echo "============================================"
echo ""
echo "App location:"
echo "  dist/NC_Simulator.app"
echo ""
echo "To run the app:"
echo "  open dist/NC_Simulator.app"
echo ""
echo "To distribute:"
echo "  Copy NC_Simulator.app to any Mac and run it!"
echo ""
