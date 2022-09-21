def is_prime(num):
    for i in range(n + 1, (n + n) ** 2):
        counter = 0
        for j in range(1, i + 1):
            if i % j == 0:
                counter +=1
        if counter == 2:
            return i

n = int(input())

print(is_prime(n))

# The get_next_prime(num) function takes a natural number
# num as an argument and returns the first prime number greater than num.