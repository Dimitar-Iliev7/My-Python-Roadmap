num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.") # Output in string


# Instructions
# Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Type a two digit number")
first_digit_number = int(two_digit_number[1])
second_digit_number = int(two_digit_number[1])
two_digit_number = first_digit_number + second_digit_number
print(type(two_digit_number)) # The result will be INTEGER (INT) 