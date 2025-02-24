data = ["Hello", "World", "Python"]

with open("output.txt", "w") as file:
    file.writelines("\n".join(data))
