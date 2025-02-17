import re

text = "Hello, world. How are you?"
pattern = r'[ ,.]'
result = re.sub(pattern, ":", text)
print(result)
