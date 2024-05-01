Instructions to prepare development environment
===============================================

Install these software:

- VS Code
- Python 3.10.10 (not newer like 3.12)
- (CMake)

  > _(likely not required, it's part of Visual Studio 2022)_

- Visual Studio 2022 ("Desktop C++" option only)

Run these commands in Powershell:

- mkdir C:\TMP
- $env:TEMP = 'C:\TMP'
     (We need to change the temp dir because compilation fails if the dirnmae is too long)
- pip install dlib

  > That's the one requiring the C++ compiler

- pip install -r requirements.txt
