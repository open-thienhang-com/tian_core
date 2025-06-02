import os
from flask import request
from datetime import datetime

def save_uploaded_file(upload_dir):
    """
    Saves an uploaded file to the specified directory.

    Args:
        upload_dir (str): The directory where the file will be saved.
        file (FileStorage): The uploaded file object obtained from Flask request.

    Returns:
        str: The file path where the file is saved.
    """
    if 'file' not in request.files:
            return "No file part in the request"
    uploaded_file = request.files['file']

    if uploaded_file.filename == '':
        return "No file selected for uploading"
    file_path = os.path.join(upload_dir, uploaded_file.filename)
    uploaded_file.save(file_path)
    return uploaded_file.filename


def list_uploaded_files(upload_dir):
    """
    List all uploaded files in the specified directory.

    Args:
        upload_dir (str): The directory where uploaded files are stored.

    Returns:
        list: A list of filenames of uploaded files.
    """
    files_info = []
    try:
        for file_name in os.listdir(upload_dir):
            file_path = os.path.join(upload_dir, file_name)
            if os.path.isfile(file_path):
                last_modified = os.path.getmtime(file_path)
                file_size_bytes = os.path.getsize(file_path)
                file_info = {
                    "name": file_name,
                    "size": file_size_bytes / (1024 * 1024),
                    "last_modified": datetime.fromtimestamp(last_modified).strftime('%Y-%m-%d %H:%M:%S'),
                    "file_path":file_path
                }
                files_info.append(file_info)
        return files_info
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
