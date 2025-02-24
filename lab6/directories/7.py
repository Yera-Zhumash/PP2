src = "source.txt"
dest = "destination.txt"

with open(src, "r") as source, open(dest, "w") as destination:
    destination.write(source.read())
