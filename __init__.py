# Blender Quick Reference Addon
# Version: 1.0.0
# Author: Sinan UYGUN
# Description: Add options to paste clipboard images as reference.
# Useful for quickly adding references from the clipboard to the scene.
# Requires 'pywin32', 'requests', 'numpy', 'pillow' libraries in Blender's Python environment.
# Installation:
#  1. Download the repository as a zip file and extract it to the Blender addons folder (or simply go to preferences and add the addon.).
#  2. If the required libraries are not installed, they will be automatically installed.
#  3. Enable the addon in 'User Preferences > Addons > Quick Reference'.
# Location: View3D > Add > Image
# Category: Import-Export

# comments added by ai


bl_info = {
    "name": "Quick Reference",
    "blender": (4, 2, 0),
    "version": (1, 0, 0),
    "author": "Sinan UYGUN",
    "description": (
        "Add options to paste clipboard images as reference. Useful for quickly adding references from the clipboard to the scene."
    ),
    "warning": (
        "Requires 'pywin32', 'requests', 'numpy', 'pillow' libraries in Blender's Python environment."
    ),
    "location": "View3D > Add > Image",
    "category": "Import-Export",
}

import bpy
from . import ops
import sys
import os
import subprocess

# check if 'pywin32', 'requests', 'numpy', 'pillow' libraries are installed
try:
    import win32clipboard
    import requests
    import numpy
    import PIL
except:
    python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')
    # install required packages
    python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')
    subprocess.call([python_exe, "-m", "pip", "install", "pywin32"])
    subprocess.call([python_exe, "-m", "pip", "install", "requests"])
    subprocess.call([python_exe, "-m", "pip", "install", "numpy"])
    subprocess.call([python_exe, "-m", "pip", "install", "pillow"])

def register():
    # register the addon
    ops.register()

def unregister():
    # unregister the addon
    ops.unregister()

# run the addon when this script is executed directly
if __name__ == "__main__":
    register()
