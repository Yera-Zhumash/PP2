import re

pattern = r'(?=[A-Z])'
text = "HelloWorldPython"
result = re.split(pattern, text)
print(result)
