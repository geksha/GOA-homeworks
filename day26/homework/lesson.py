# homework 1: 
# მომხმარებელს შემოატანინეთ მისი სახელი, შემდეგ დაბეჭდეთ lower, upper, capitalize ვარიანტებად.

name = input("Please enter your name: ")

print(name.lower())
print(name.upper())
print(name.capitalize())


# homework 2:
# შექმენით ფუნქცია, სახელად find_index, რომელსაც გადაეცემა სთრინგი და საპოვნელი ასო. თქვენი დავალებაა, რომ გადაცემულ სთრინგში არსებული ასოს ინდექსი დააბრუნოთ.

def find_index(word, find_char):
    for index in range(len(word))
        if word[index] == find_char:
            return index
        
print(find_index("luka", "k"))

# name = "Luka"

# print(name[2])


# homework 3:
# def keyword-ის გამოყენებით შექმენით len()-ის მსგავსი ფუნქცია (ფუნქცია რომელიც გამოიტანს რამდენი ელემენტია collection-ში)

def manual_len(collection):
    count = 0

    for item in collection:
        count = count + 1
    return count

print(manual_len(["luka", "lile", 3, True, "Nia"]))

# homework 4:


names = ["Luka", "Lile", "Nia"]

names.pop(0)

print(names)






