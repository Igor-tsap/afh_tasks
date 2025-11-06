# Write a Python code to remove characters from a string from 0 to n and return a new string.
# Use string slicing to get a substring.
# Think about how you can use the slicing notation [:] along with the value of n
# to select the portion of the string after the first n characters.
# Given:
#
def remove_chars(word, n):
    return word[n:]

print("Removing characters from a string")
print(remove_chars("pynative", 4))
# output 'tive' first four characters are removed

print(remove_chars("pynative", 2))
# output 'native'
