# This module contains functions to get clipboard contents.
# It uses the win32clipboard module.

import win32clipboard
import tempfile

from PIL import ImageGrab, Image
import io


dataUsingChromium = False

# Panodaki resmi almak için
def get_clipboard_image_chromium():
    # Resmi panodan al
    image = ImageGrab.grabclipboard()
    if image is None:
        return None
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        image.save(temp_file, format='PNG')
        temp_file_path = temp_file.name
    return {'path': temp_file_path, 'chromium': True}

# Function to get file paths from clipboard.
def get_file_paths_from_clipboard():
    """
    Get file paths from clipboard.
    """
    # Open clipboard.
    win32clipboard.OpenClipboard()
    
    try:
        # Check if clipboard contains file paths.
        if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_HDROP):
            # Get file paths.
            file_paths = win32clipboard.GetClipboardData(win32clipboard.CF_HDROP)
            return file_paths
    finally:
        # Close clipboard.
        win32clipboard.CloseClipboard()
    
    # If clipboard does not contain file paths, return None.
    return None

# Function to get clipboard text.
def get_clipboard_text():
    global dataUsingChromium
    """
    Get clipboard text.
    """
    # Open clipboard.
    win32clipboard.OpenClipboard()
    
    try:
        # Check if clipboard contains unicode text.
        if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_UNICODETEXT):
            # Get unicode text.
            data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
        # Check if clipboard contains text.
        elif win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_TEXT):
            # Get text.
            data = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
        # if user uses chromium
        elif win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_BITMAP):
            data = get_clipboard_image_chromium()
        else:
            # If clipboard does not contain text, return None.
            return None
        if type(data) == dict:
            dataUsingChromium = True
            return data['path']
        else:
            dataUsingChromium = False
            return data
    finally:
        # Close clipboard.
        try:
            win32clipboard.CloseClipboard()
        except:
            pass

# Function to get default clipboard content.
def get_default():
    """
    Get default clipboard content.
    """
    # Get file paths from clipboard.
    file_paths = get_file_paths_from_clipboard()
    
    # Initialize default variable.
    default = None
    
    # If clipboard contains file paths, set default to the first file path.
    if file_paths:
        for path in file_paths:
            default = path
    else:
        # If clipboard does not contain file paths, get clipboard text.
        clipboard_data = get_clipboard_text()
        if clipboard_data:
            default = clipboard_data
        else:
            # If clipboard does not contain text, set default to None.
            default = None
    
    # Check if default is a valid image file or URL.
    if (default and
        (default.endswith('.png') or default.endswith('.jpg') or default.endswith('.webp') or default.endswith('.jpeg')) and
        (default.startswith('https://') or default.startswith('http://'))):
        return {'content': default, 'type': 'IMAGE_URL'}
    # Check if default is a valid image file.
    elif (default and
          (default.endswith('.png') or default.endswith('.jpg') or default.endswith('.webp') or default.endswith('.jpeg'))):
        if dataUsingChromium == True:
            return {'content': default, 'type': 'IMAGE_FILE', 'chromium': True}
        else:
            return {'content': default, 'type': 'IMAGE_FILE', 'chromium': False}

    else:
        # If default is not a valid image file or URL, set type to 'NONE_TYPE'.
        return {'content': default, 'type': 'NONE_TYPE'}
