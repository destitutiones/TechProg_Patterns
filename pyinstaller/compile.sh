#!/usr/bin/env bash
mv assembly.py assembly.spec
pyinstaller --onefile assembly.spec
rm -rf build
rm -rf __pycache__
mv assembly.spec assembly.py
