# Problem Solving Problems part 2!

# Problem #1 - Happy Numbers



happy_number = input("Enter a number to see if it's happy! ")

def first_mode(happy_number):        #Takes first number and breaks it into separate integers.
    for number in str(happy_number):
        broken_integer.append(int(number))

def second_mode(broken_integer):      #Takes those separate integers and squares each one.
    for number in broken_integer:
        next_step.append(int(number * number))

def numbers(next_step):
    last_count = 0                   #Returns the sum of the squared integers.
    for number in next_step:
        last_count += number
    return last_count


def final_check(final_sum):
    if final_sum == 1:                                 #Determination stage of the final sum of squared integers.
        print("Your number is a happy number!")
    elif final_sum == happy_number:
        print("Your number is not a happy number.")
    elif final_sum == final_sum:
        print('Your number is not a happy number.')
    elif final_sum != 1:
        broken_integer = []
        next_step.clear()
        first_mode(final_sum)
        second_mode(broken_integer)
        final_sum = numbers(next_step)
        final_check(final_sum)

broken_integer = []
next_step = []

first_mode(happy_number)
second_mode(broken_integer)
final_sum = numbers(next_step)
final_check(final_sum)


# Problem #2 - Prime Numbers

def initial_number():
    for number in range(2, 101):          #Started at 2 since 0 and 1 cannot be prime numbers.
        for digit in range(2, number):
            if number % digit == 0:       #As the number increases, this is looking for any possible way to make factors of the number.
                break
        else:
            print(number)


initial_number()


# Problem #3 - Fibonacci Sequence


def fibonacci(user_num):
    number_one = 0           #Initial start of the Fibonacci chain.
    number_two = 1
    added_result = 0
    for number in range(user_num):
        print(added_result)           #The daisy chain that loops the sequence, making the Fibonacci chain work.
        number_one = number_two
        number_two = added_result
        added_result = number_one + number_two

user_num = int(input("How many sequences would you like to iterate? "))
fibonacci(user_num)