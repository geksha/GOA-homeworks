# Homework 1
# Code Wars
# Who likes it?, 6 kyu

def likes(names):
    if names==[]:
        return "no one likes this"
    elif len(names)==1:
        return names[0]+" likes this"
    elif len(names)==2:
        return names[0]+ " and "+names[1]+" like this"
    elif len(names)==3:
        return names[0]+", "+names[1]+" and "+names[2]+" like this"
    elif len(names)>3:
        return names[0]+", "+names[1]+" and "+ str(len(names)-2)+" others like this"
    pass

# Homework 2
# Multiples of 3 or 5, 6 kyu

def solution(number):
    result = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)

    return sum(result)



