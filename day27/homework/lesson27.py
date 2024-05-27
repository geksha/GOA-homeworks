# Homework 1:

# Create a function that returns the sum of the two lowest positive numbers given
# an array of minimum 4 positive integers. No floats or non-positive integers will be passed

# def sum_two_smallest_numbers(numbers):
#     numbers.sort()
#     return numbers[0] + numbers[1]


# Homework 2:

# Make a program that filters a list of strings and returns a list with only your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
# Otherwise, you can be sure he's not...

# def friend(x):
#     friends = []
    
#     for name in x:
#         if len(name) == 4:
#             friends.append(name)
            
#     return friends


# Homework 3:

# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

# def find_short(s):
#     words_list = s.split()
    
#     min_length = len(words_list[0])
    
#     for word in words_list:
#         if min_length > len(word):
#             min_length = len(word)
            
#     return min_length


# Homework 4:

# You are going to be given a word. Your job is to return the middle character of the word.
# If the word's length is odd, return the middle character. If the word's length is even,
# return the middle 2 characters.

# def get_middle(s):
#     word_length = len(s)
#     index = word_length // 2 
    
#     if word_length % 2 == 0:
#         return s[index - 1] + s[index]
    
#     return s[index]


# Homework 5:

# In this little assignment you are given a string of space separated numbers,
# and have to return the highest and lowest number.

# def high_and_low(numbers):
#     strings_list = numbers.split(" ")
#     numbers_list = []
    
#     for number in strings_list:
#         numbers_list.append(int(number))
    
#     print(numbers_list)
    
#     return str(max(numbers_list)) + " " + str(min(numbers_list))