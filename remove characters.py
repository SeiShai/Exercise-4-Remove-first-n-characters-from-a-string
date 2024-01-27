# Write a program to remove characters from a string
# starting from zero up to n and return a new string.

# Ask for input
word = str(input('Enter a word: '))
number_of_characters = int(input('Enter a number: '))

# function
def remove_characters(word, number_of_characters):
    print('Chosen word: ', word)
    result = word[number_of_characters:]
    return result

print(remove_characters(word, number_of_characters))