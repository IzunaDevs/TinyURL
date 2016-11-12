@echo off
"%SystemDrive%\Python352\python.exe" setup.py sdist
"%SystemDrive%\Python352\python.exe" setup.py bdist_wheel
"%SystemDrive%\Python352\python.exe" -m twine upload "dist/*"
pause