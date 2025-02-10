#Implement a generator that returns all numbers from (n) down to 0.

def countdown(n):
    for i in range(n, -1, -1):
        yield i

# Example usage
n = 10
for num in countdown(n):
    print(num)
