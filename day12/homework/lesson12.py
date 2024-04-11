'''person_info = []

name = input("Please enter your name: ")
lastname = input("Please enter your lastname: ")
age = int(input("Please enter your age: "))
address = input("Please enter your address: ")

person_info.append(name)
person_info.append(lastname)
person_info.append(age)
person_info.append(address)

print(person_info)
print(person_info[0:2])
print(person_info[1:3])
print(person_info[0:3])
print(person_info[1:])'''

'''num = int(input("Please enter negative number: "))

negative_numbers = []

for i in range(num,0):
    negative_numbers.append(i)

print(negative_numbers)'''

'''fullname = "Gega Devdariani"

print(fullname[:4])
print(fullname[5:])'''

#სიაში შეინახეთ მინიმუმ 5 საყვარელი ფილმი. გამოიყენეთ Slicing და დაბეჭდეთ რამდენიმე კომბინაციით.
#Bonus (არ არის აუცილებელი): იგივე კომბინაციები დაბეჭდეთ უარყოფითი ინდექსების გამოყენებით. 

list = ['harry poter', 'breaking bad', 'avatar', 'home alone']

print(list[0:2])
print(list[2:4])
print(list[1:4])
print(list[-5:-3])
print(list[-3:-1])
print(list[-4:-1])