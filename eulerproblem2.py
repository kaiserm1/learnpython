# Fibonacci sequence: Each new term is the sum of it's previous two terms, starting with 1 and 2

fibonacci_sequence = [1, 2]
next_term = 0

for num in range(0,100):
    if num > 1:
        next_term = fibonacci_sequence[num-2] + fibonacci_sequence[num-1]
        if next_term < 4000000:
            fibonacci_sequence.append(next_term)
        else:
            break

result = 0

for num2 in range(0,len(fibonacci_sequence)):
    if fibonacci_sequence[num2] % 2 == 0:
        result = result + fibonacci_sequence[num2]

print(result)
