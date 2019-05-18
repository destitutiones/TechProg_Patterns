move assembly.py assembly.spec
pyinstaller --onefile assembly.spec
rmdir /Q /S build
rmdir /Q /S __pycache__
move assembly.spec assembly.py
