import re

pattern = r'[A-Z][a-z]+'
test_strings = ["Hello", "hello", "A", "ABC", "Python"]
for s in test_strings:
    print(f"{s}: {bool(re.fullmatch(pattern, s))}")
