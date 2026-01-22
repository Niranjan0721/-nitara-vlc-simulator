# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec file for macOS

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['serial.tools.list_ports'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='NC_Simulator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=True,  # Important for macOS
    target_arch=None,  # Will build for current architecture (Intel or Apple Silicon)
    codesign_identity=None,
    entitlements_file=None,
)

# macOS specific: Create .app bundle
app = BUNDLE(
    exe,
    name='NC_Simulator.app',
    icon=None,  # Add icon path here if you have one: 'icon.icns'
    bundle_identifier='com.nitara.vlcsimulator',
    info_plist={
        'CFBundleName': 'NC Simulator',
        'CFBundleDisplayName': 'NC Simulator',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHighResolutionCapable': True,
        'LSMinimumSystemVersion': '10.13.0',
    },
)
