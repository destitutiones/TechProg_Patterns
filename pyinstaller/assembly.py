# -*- mode: python -*-

block_cipher = None

a = Analysis(
    ['../main.py'],
    pathex=['../'],
    binaries=None,
    hiddenimports=[],
    hookspath=None,
    runtime_hooks=None,
    excludes=None,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher
)

pyz = PYZ(
    a.pure, a.zipped_data,
    cipher=block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='TP_Patterns',
    debug=False,
    strip=False,
    upx=False,
    runtime_tmpdir=None,
    console=True
)
