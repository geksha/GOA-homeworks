def to_jaden_case(string):
    return ' '.join(i.capitalize() for i in string.split())




# დავალება: 








# გზა 2
# string = ""
# string += "how".capitalize() + " "
# string += "can".capitalize()

# print(string)

# გზა 3
# listn = []
# listn.append("how".capitalize())
# listn.append("can".capitalize())

# print(" ".join(listn))

def to_jaed_case(string):
    listn = string.split()
    result = []
    for i in listn:
        cap_string = i.capitalize()
        result.append(cap_string)
    return " ".join(result)
    
