import os

path = "example.txt"  # Укажите нужный путь

if os.path.exists(path):
    print("File exists")
    print("Directory:", os.path.dirname(path))
    print("Filename:", os.path.basename(path))
else:
    print("Path does not exist")
