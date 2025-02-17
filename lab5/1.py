import re

pattern = r'ab*'
test_strings = ["a", "ab", "abb", "ac", "abc"]
for s in test_strings:
    print(f"{s}: {bool(re.fullmatch(pattern, s))}")
