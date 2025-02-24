file_path = "example.txt"  # Укажите нужный путь

with open(file_path, "r") as file:
    line_count = sum(1 for _ in file)

print("Number of lines:", line_count)
