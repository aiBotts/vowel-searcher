# This program finds the number of vowels in a string.

def main():
    # Display how many A's are in the string.
    vowelA()
    # Display how many E's are in the string.
    vowelE()
    # Display how many I's are in the string.
    vowelI()
    # Display how many O's are in the string.
    vowelO()
    # Display how many U's are in the string.
    vowelU()

def vowelA():
    # Create a variable to hold the count.
    # The variable must start with 0.
    count = 0

    # Ask the user for a string.
    my_string = input("Enter a string: ")

    for Aa in my_string:

        # Find out how many A's are in the string
        if Aa == "A" or Aa == "a":
            count += 1
    print('a: ', count)

def vowelE():
    # Create a variable to hold the count.
    # The variable must start with 0.
    count = 0

    # Ask the user for a string.
    my_string = input('Enter a string: ')

    # Find out how many E's are in the string
    for Ee in my_string:
        if Ee == "E" or Ee == "e":
            count += 1
    print('e: ', count)

def vowelI():
    # Create a variable to hold the count.
    # The variable must start with 0.
    count = 0

    # Ask the user for a string.
    my_string = input('Enter a string: ')

    # Find out how many I's are in the string
    for Ii in my_string:
        if Ii == "I" or Ii == "i":
            count += 1
    print('i: ', count)

def vowelO():
    # Create a variable to hold the count.
    # The variable must start with 0.
    count = 0

    # Ask the user for a string.
    my_string = input('Enter a string: ')

    # Find out how many O's are in the string
    for Oo in my_string:
        if Oo == "0" or Oo == "o":
            count += 1
    print('o: ', count)

def vowelU():
    # Create a variable to hold the count.
    # The variable must start with 0.
    count = 0

    # Ask the user for a string.
    my_string = input('Enter a string: ')

    # Find out how many U's are in the string
    for Uu in my_string:
        if Uu == "U" or Uu == "u":
            count += 1
    print('u: ', count)

# Call the function
main()