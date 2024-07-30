# Blender Quick Reference Add-on

This Add-on is designed to streamline the process of importing images from your clipboard directly into Blender as reference images. Quick Reference supports copying images directly from any browser via right-click and pasting them into Blender, as well as pasting links from the clipboard to import the corresponding images.

## Features

- Import images directly from the clipboard as references in Blender
- Support for copying images from any browser via right-click copy.
- Paste links from the clipboard to import images into Blender

## Installation

1. Download the repository as a ZIP file.
2. Open Blender.
3. Open Scripts, run the code below.
4. Restart Blender.
5. Go to `Edit` > `Preferences` > `Add-ons`.
6. Click `Install` and select the downloaded ZIP file.
7. Enable the add-on from the list.

### Prerequisites

Before installing the add-on, you need to ensure that the required Python packages are installed in Blender's Python environment. Run the following script in Blender's Python console and `restart blender`.:

```python
import subprocess
import sys

def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"Successfully installed {package}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package}: {e}")

install('pillow')
install('requests')
install('numpy')
install('pywin32')
```

## Usage

1. Copy an image or image link from your browser.
3. Use the add-on to paste the image or link as a reference.

Once installed, the add-on will be available in the View3D > Add > Image (CTRL + A > Image).
![Screenshot](https://github.com/sinanuygunn/blender_quick_reference/blob/main/screenshots/Screenshot.png)
![Screenshot2](https://github.com/sinanuygunn/blender_quick_reference/blob/main/screenshots/Screenshotcat2.png)

## Supported Platforms

This Add-on has been tested only on Windows. It has not been tested on other platforms (macOS, Linux, etc.), and it is likely that it will not work on these platforms.


