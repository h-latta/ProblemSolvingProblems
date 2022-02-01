# Problem Solving Problems part 2!
# WHITEBOARD CHALLENGES!


#Problem #1 - Target Number in an Array

number_array = [5, 17, 77, 50]


#Problem #2 - Palindromes

palindrome = input("Let's see if your word is a palindrome! ")
word_check = palindrome[::-1] 

if word_check != palindrome:
    print("Your word isn't a palindrome!")
else:
    print("Your word is a palindrome.")

#Problem #3 - Incrementing Integers



#Problem #4 - Positive Sum, Negative Sum

list_of_numbers =  [7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21]

def number_sort(list_of_numbers):
    positive_sum = 0
    negative_sum = 0
    for number in list_of_numbers:
        if number > 0:
            positive_sum += number
        elif number < 0:
            negative_sum += number
    print(positive_sum)
    print(negative_sum)

number_sort(list_of_numbers)

#Problem #5 - High and Low Numbers



#Problem #6 - Email Validation



#Problem #7 - Letters to Numbers



#Problem #8 - Rolling Lock



#Problem #9 - Happy Numbers Part 2



#Problem #10 - Reciprocal of the Reverse