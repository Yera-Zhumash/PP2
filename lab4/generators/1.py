#Create a generator that generates the squares of numbers up to some number N.

def square_generator(N):
    for i in range(N + 1):
        yield i * i

# Example usage
N = 5
for square in square_generator(N):
    print(square)
