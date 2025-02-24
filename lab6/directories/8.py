import os

file_path = "file_to_delete.txt"  # Укажите нужный путь

if os.path.exists(file_path) and os.access(file_path, os.W_OK):
    os.remove(file_path)
    print("File deleted")
else:
    print("Cannot delete file")
