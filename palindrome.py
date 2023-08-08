def reverse_string(input_string):
    return input_string[ ::-1] #start stop step

input_string = input('Enter the string: ')
reversed_string = reverse_string(input_string)

if input_string == reversed_string :
    print('yes, the given input string is a palindrome')

else:
    print('no, the given input string is not a palindrome')
