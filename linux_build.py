import os
from cx_Freeze import setup, Executable

# Add assets folder to include files
assets_folder = 'assets'
assets_files = [(os.path.join(assets_folder, f), os.path.join(assets_folder, f)) for f in os.listdir(assets_folder)]

# Build options
build_exe_options = {
    'includes': ['pygame'],
    'include_files': assets_files,
}

# Executable
exe = Executable(
    script='main.py',
    target_name='my_game',
)

# Setup cx_Freeze
setup(
    name='My Game',
    version='1.0',
    description='My Pygame game',
    options={
        'build_exe': build_exe_options,
    },
    executables=[exe],
)

#command python linux_build.py build

