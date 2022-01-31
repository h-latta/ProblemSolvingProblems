

# Problem 1 - Reverse a string!

from itertools import count, groupby  # Tried using some other imported tools to count the letters.
from tokenize import group


normal_string = input('Enter any word you like. ')
final_string = normal_string[::-1] #Discovered slice notation.. mind blown
print(final_string)


# Problem 2 - Capitalize letter!

lowercase_string = input('Type in some words you want capitalized. ')
capitalized_words = lowercase_string.title() #Finding all kinds of cool commands...
print(capitalized_words)


# Problem 3 - Compressing a string of characters!


group_of_letters = input('Smash your keyboard so you get a bunch of random letters. ')
letter_list = ""
count = 1

for letter in range(len(group_of_letters)-1): 
    if group_of_letters[letter] == group_of_letters[letter+1]: # Counting for duplicate letters
        count = count + 1
    else:
        letter_list = letter_list + str(count) + group_of_letters[letter] #Accounting for non-repeating letters
        count = 1

letter_list = letter_list + str(count) + group_of_letters[letter+1]

print(letter_list)



# Problem 4 - Palindromes...


palindrome = input("Let's see if your word is a palindrome! ")
word_check = palindrome[::-1]  # The reversal trick from problem 1!!

if word_check != palindrome:
    print("Your word isn't a palindrome!")
else:
    print("Your word is a palindrome.")