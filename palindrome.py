a_string = 'Was it a car or a cat I saw'
def palindrome(string):
    string = string.lower().replace(' ', '')
    return string == string[::-1]
print(palindrome(a_string))
# Returns: True


a_string = 'Was it a car or a cat I saw'
def palindrome(string):
    string = string.lower().replace(' ', '')
    reversed_string = ''.join(reversed(string))
    return string == reversed_string
print(palindrome(a_string))
# Returns: True

# for loop
a_string = 'Was it a car or a cat I saw'
def palindrome(string):
    string = string.lower().replace(' ', '')
    reversed = ''
    for i in range(len(string), 0, -1):
        reversed += string[i-1]
    return string == reversed
print(palindrome(a_string))

# Use a While Loop in Python to check if a String is a Palindrome
a_string = 'Was it a car or a cat I saw'
def palindrome(string):
    string = string.lower().replace(' ', '')
    first, last = 0, len(string) - 1
    while(first < last):
        if(string[first] == string[last]):
            first += 1
            last -= 1
        else:
            return False
    
    return True
print(palindrome(a_string))
# Returns: True


a_number = 123454321
def palindrome(number):
    number = str(number)
    return number == number[::-1]
print(palindrome(a_number))
# Returns: True