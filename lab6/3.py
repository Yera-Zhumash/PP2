def is_palindrome(s):
    return s == s[::-1]

word = "radar"
print(is_palindrome(word))  # Вывод: True
