# This module contains functions to get clipboard contents.
# It uses the win32clipboard module.

import win32clipboard

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
        else:
            # If clipboard does not contain text, return None.
            return None
        return data
    finally:
        # Close clipboard.
        win32clipboard.CloseClipboard()

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
        return {'content': default, 'type': 'IMAGE_FILE'}
    else:
        # If default is not a valid image file or URL, set type to 'NONE_TYPE'.
        return {'content': default, 'type': 'NONE_TYPE'}
