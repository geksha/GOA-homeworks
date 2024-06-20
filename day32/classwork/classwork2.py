

#def square_digits(num):
#    num = str(num)
#    result = ''
#    for i in num:
#        result += str(int(i)**2)
#    return int(result)
#var = square_digits(123)
#print(var)

def square_digits(num):
    result = ''
    for digit in str(num):
        result += str(int(digit) ** 2)
    return int(result)