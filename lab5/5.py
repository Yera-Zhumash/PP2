import re

pattern = r'a.*b$'
test_strings = ["ab", "acb", "a123b", "abc", "a_b"]
for s in test_strings:
    print(f"{s}: {bool(re.fullmatch(pattern, s))}")
