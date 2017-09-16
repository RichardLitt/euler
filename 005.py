# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def divisable():
    # Go from this number
    iterator = 500
    found_number = 0
    # While we haven't found the number
    while (iterator != found_number):
        # Assume the number works
        number_doesnt_work = False
        # For all divisors
        for x in range(1,21):
            # If there is something left over
            if (iterator % x != 0):
                # State the the number doesn't work
                number_doesnt_work = True
                # Go to the next number we're looking for
                iterator += 1
                # Break out of this for loop without testing another divisor
                break
        # If it never breaks
        else:
            # Stop and print.
            found_number = iterator
    print found_number

divisable()