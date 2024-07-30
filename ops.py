# Import necessary modules
import bpy
import os
from .getclipboard import get_default
from PIL import Image as PILImage
from .utils import download_image, create_image_from_data
import io

# Define the operator class
class OBJECT_OT_add_clipboard_image_as_reference(bpy.types.Operator):
    # Define the operator properties
    bl_idname = "object.add_clipboard_image_as_reference"
    bl_label = "Add Clipboard Image as Reference"
    bl_description = "Add the clipboard image as a reference image"

    # Define the operator method
    def execute(self, context):
        # Get the clipboard data
        data = get_default()

        # Check if the clipboard data is a file
        if data['type'] == 'IMAGE_FILE':
            image_path = data['content']

            # Check if the file exists
            if os.path.exists(image_path):
                # Load the image file
                bpy.data.images.load(image_path)

                with open(image_path, "rb") as f:
                    image_data = f.read()
                    imageWithSaved = create_image_from_data(io.BytesIO(image_data))
                    
                # Create an empty object with the image data
                empty = bpy.data.objects.new("ReferenceImage", None)
                context.collection.objects.link(empty)
                empty.empty_display_size = 5  # Adjust size as needed
                empty.empty_display_type = 'IMAGE'
                empty.data = imageWithSaved
                empty.rotation_euler[0] = 3.141592653589793 # 180 degrees (pi)
            else:
                self.report({'WARNING'}, "File does not exist.")

        # Check if the clipboard data is a URL
        elif data['type'] == 'IMAGE_URL':
            image_data = download_image(data['content'])

            # Check if the image is successfully downloaded
            if image_data:
                image = create_image_from_data(image_data)
                empty = bpy.data.objects.new("ReferenceImage", None)
                context.collection.objects.link(empty)
                empty.empty_display_size = 5  # Adjust size as needed
                empty.empty_display_type = 'IMAGE'
                empty.data = image
                empty.rotation_euler[0] = 3.141592653589793 # 180 degrees (pi)
            else:
                self.report({'WARNING'}, "Failed to download image.")

        # If the clipboard data is not a valid image, report a warning
        else:
            self.report({'WARNING'}, "Clipboard does not contain a valid image.")

        # Return the completion status
        return {'FINISHED'}

# Define the menu function
def menu_func(self, context):
    layout = self.layout
    layout.operator("object.add_clipboard_image_as_reference")

# Define the registration and unregistration functions
def register():
    bpy.utils.register_class(OBJECT_OT_add_clipboard_image_as_reference)
    bpy.types.VIEW3D_MT_image_add.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_clipboard_image_as_reference)
    bpy.types.VIEW3D_MT_image_add.remove(menu_func)