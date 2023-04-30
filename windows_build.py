import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["pygame"],
    "include_files": ["assets/"],
    "excludes": ["tkinter"]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="MyGame",
    version="1.0",
    description="My awesome game",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, targetName="MyGame.exe")]
)

#command python windows_build.py build_exe --build-exe MyGame.exe


