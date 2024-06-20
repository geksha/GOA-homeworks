#Homework 1:
#List Filtering

def high_and_low(numbers):
    numbers = numbers.split(" ")
    numbers = sorted(numbers, key=int)
    return numbers[-1] + " " + numbers[0]