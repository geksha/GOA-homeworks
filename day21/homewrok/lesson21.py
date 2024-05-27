# Homewok 1:

# Given a non-empty array of integers
# return the result of multiplying the values together in order.


# def grow(arr):
#     num_list = []
#     filtered_list = []
    
#     for num in arr:
#         num_list.append(num)
#     print(num_list)
    
#     for multiplication in range(grow):
#         filtered_list.append(num_list(num))
#     return filtered_list

# my_arr = [1,2,3,4,5,6,7,8,9]

# print((my_arr()))

# Homework 2:

# Write function bmi that calculates body mass index (bmi = weight / height2).

# def bmi(weight, height):
#     bmii = weight / height ** 2
    
#     if bmii <= 18.5:
#         return "Underweight"

#     if bmii <= 25.0: 
#         return "Normal"

#     if bmii <= 30.0:
#         return "Overweight"

#     if bmii > 30:
#         return "utra obese"


# Homework 3:

# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

# def get_count(sentence):
#     my_arr = []
#     filtered_list = []
    
#     for i in sentence:
#         my_arr.append(i)
        
#     for word in range(my_arr(["a", "e", "i", "o", "u"])):
#         filtered_list.append(word)

#     return filtered_list

# sentence = ["audi", "bmw", "anmier"]

# print(sentence)

# Homework

# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out,
#  because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625
# because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

# Note: The function accepts an integer and returns an integer.

# def square_digits(num):
#     num = str(num)
#     num = list(num)
    
#     new_arr = []
    
#     for i in num:
#         new_arr.append(int(i))
        
#     new_str = ""
#     for i in new_arr:
#         squared = i ** 2
#         new_str += str(squared)
#     return int(new_str)

# Homework 5:

# Your task is to make a function that can take
# any non-negative integer as an argument and return
# it with its digits in descending order.
#  Essentially, rearrange the digits to create the highest possible number

# def descending_order(num):
#     num = str(num)
#     num = list(num)
    
#     new_arr = []    
#     for i in num:
#         new_arr.append(int(i))
#     new_arr.sort(reverse = True)
    
    
#     res_str = ""
#     for x in new_arr:
#         res_str += str(x)
#     return int(res_str)

# Homework 6:

# You probably know the "like" system from Facebook, Instagram and other pages.
# People can "like" blog posts, pictures or other items.
# We want to create the text that should be displayed next to such an item

# def likes(names):
#     if names == []:
#         return "no one likes this"
#     elif len(names) == 1:
#         return names[0] + " likes this"
#     elif len(names) == 2:
#         return names[0] + " and " + names[1] + " like this"
#     elif len(names) == 3:
#         return names[0] + ", " + names[1] + " and " + names[2] + " like this"
#     else:
#         return names[0] + ", " + names[1] + " and " + str(len(names) -2) + " others like this"
    


# Homewrok 7:

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Finish the solution so that it returns the sum
# of all the multiples of 3 or 5 below the number passed in.

# Additionally, if the number is negative, return 0.

# Note: If the number is a multiple of both 3 and 5, only count it once

# def solution(number):
#     sum = 0
    
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             sum += i
#     return sum