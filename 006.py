# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 == 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Sum of the squares of all of the numbers
def sum_of_squares(stop):
    sum = 0
    for x in range(1,stop+1):
        sum += (x*x)
    print sum
    return sum

def square_of_sums(stop):
    sum = 0
    for x in range(1,stop+1):
        sum += x
    sum = sum**2
    print sum
    return sum

result = square_of_sums(100) - sum_of_squares(100)
print result
