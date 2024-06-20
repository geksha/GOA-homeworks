# [[], []]
# 1st way

listm = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2st way

# append - ამატებს სიაში ელემენტს ბოლოში

listn = []

for i in range(10):
    listn.append("GOA")

print(listn)

listq = ['apple']

listq.append('banana')

print(listq)
print(listq[1])

# def - define
# len - lenght

listo = ['apple', 15, 15,5, True]

lenght = len(listo)

print(lenght)

string = "apple"

print(len(string))

#def add_list(count)
#    listm = []
#
#    for i in range(count):
#        listm.append(i)
#    return listm

#print(add_list(5))
#print(add_list(10))

# lists are mutable
# string are immutable

#listn = ['thor', 'iron man', 'captain america']
#          0         1               2 
#print(listn[2])
#       ['thor', 'interstellar', 'iron man', 'captain america']
# listn.insert(2, 'interstellar')

# print(listn)
# print(listn[3])

listn = ['thor', 'iron man', 'captain america']
#          0         1               2
#      ['thor', 'captain america']
listn.pop(2)

print(listn)

# pop - არის ფუნქცია რომელსაც არგუმენტი თუ არ მივუთითეთ ამოშლის ბოლო ელემენტს