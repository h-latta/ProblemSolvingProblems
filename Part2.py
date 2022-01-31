# Problem Solving Problems part 2!

# Problem #1 - Happy Numbers

from itertools import count


happy_number = input("Enter a number to see if it's happy! ")

def first_mode(happy_number):
    for number in str(happy_number):
        broken_integer.append(int(number))

def second_mode(broken_integer):
    for number in broken_integer:
        next_step.append(int(number * number))

def numbers(next_step):
    count == 0
    for number in next_step:
        count == count + number
        return count


def final_check(number_sum):
    if number_sum != 1:
        broken_integer = [number_sum]
        next_step.clear()
        first_mode(number_sum)
        second_mode(broken_integer)
        numbers(next_step)
        final_check(final_sum)
    elif number_sum == happy_number:
        print("Your number is not a happy number.")
    elif number_sum == 1:
        print("Your number is a happy number!")

broken_integer = []
next_step = []
final_sum = numbers(next_step)

first_mode(happy_number)
second_mode(broken_integer)
numbers(next_step)
final_check(final_sum)


# Problem #2 - Prime Numbers





# Problem #3 - Fibonacci Sequence