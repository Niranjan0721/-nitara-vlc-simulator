#!/bin/bash
echo "=== NC Simulator - Building macOS .app Bundle ==="
echo ""

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 is not installed!"
    echo "Please install Python3 from https://www.python.org/downloads/"
    exit 1
fi

# Check if pyinstaller is installed
if ! command -v pyinstaller &> /dev/null; then
    echo "Installing PyInstaller..."
    pip3 install pyinstaller
fi

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build dist

echo ""
echo "Building macOS .app bundle using spec file..."
echo ""

# Build using the macOS spec file
pyinstaller NC_Simulator_macos.spec

echo ""
echo "============================================"
echo "BUILD COMPLETE!"
echo "============================================"
echo ""
echo "App bundle location:"
echo "  dist/NC_Simulator.app"
echo ""
echo "To run:"
echo "  open dist/NC_Simulator.app"
echo ""
echo "To install for all users:"
echo "  sudo cp -r dist/NC_Simulator.app /Applications/"
echo ""
echo "To create a DMG for distribution:"
echo "  hdiutil create -volname 'NC Simulator' -srcfolder dist/NC_Simulator.app -ov NC_Simulator.dmg"
echo ""
