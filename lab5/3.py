import re

pattern = r'[a-z]+_[a-z]+'
test_strings = ["hello_world", "helloWorld", "abc_def_ghi", "_underscore"]
for s in test_strings:
    print(f"{s}: {bool(re.search(pattern, s))}")
