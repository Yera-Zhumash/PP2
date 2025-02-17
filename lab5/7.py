import re

def snake_to_camel(snake_str):
    return ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(snake_str.split('_')))

print(snake_to_camel("hello_world"))
