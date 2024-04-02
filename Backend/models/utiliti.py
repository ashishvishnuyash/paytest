import os
import uuid
directory = '../media/'
def save_media_file(binary_data):
    """
    Saves binary data of a media file to a unique filename in the specified directory.
    The file extension is preserved.

    Parameters:
    binary_data (bytes): The binary data of the media file.
    directory (str, optional): The directory where the file will be saved. Defaults to './'.

    Returns:
    str: The unique filename with preserved file extension.
    """
    try:
        # Generate a unique filename
        file_extension = get_file_extension(binary_data)
        unique_filename = f"{uuid.uuid4().hex}.{file_extension}"

        # Construct the full path to save the file
        save_path = os.path.join(directory, unique_filename)

        # Save the binary data to the file
        with open(save_path, 'wb') as file:
            file.write(binary_data)
        
        return save_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_file_extension(binary_data):
    """
    Extracts and returns the file extension from binary data.

    Parameters:
    binary_data (bytes): The binary data of the media file.

    Returns:
    str: The file extension (e.g., 'jpg', 'png').
    """
    # Define magic numbers for common file types
    file_types = {
        b'\xFF\xD8\xFF': 'jpg',
        b'\x89PNG': 'png',
        # Add more file types as needed
    }

    # Check the magic number to determine the file type
    for magic_number, file_extension in file_types.items():
        if binary_data.startswith(magic_number):
            return file_extension
    
    # Default to 'bin' if file type is unknown
    return 'bin'


