# What is the 10001st prime?
# Import library to read from terminal
import sys

# Find if a number is prime
def is_prime(num):
    if (num == 2):
        return True
    for x in range(2, num/2+1):
        if (num % x == 0):
            return False
    else:
        return True

# List all primes in order
def list_primes(stop):
    found = 0
    current_num = 2
    while (found != stop):
        if (is_prime(current_num)):
            found += 1
        previous_num = current_num
        current_num += 1
    print previous_num

list_primes(int(sys.argv[1]))
