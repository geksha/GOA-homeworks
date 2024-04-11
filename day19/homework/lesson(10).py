#მომხმარებელს შემოატანინეთ ხუთი სიტყვა და ყველა მათგანი დაამატეთ ერთ სიაში. შემდეგ შეეკითხეთ შესაერთებელი მნიშვნელობა, მაგ. "-" / "+" / "^" და ა.შ. თქვენი დავალებაა რომ იმუშავოთ სიაზე: მხოლოდ ლუწ ინდექსიან სიტყვებს დაუწეროთ ბოლოში ეს დასაკავშირებელი მნიშვნელობა და შემდეგ დაამატოთ საერთო სთრინგში. საბოლოოდ კი უნდა დაბეჭდოთ ეს სთრინგი. Test case: input) ("python", "html", "css", "js", "git"), "+" -> output) "python+css+git".

'''string_list = []

for i in range(5):
    word = input("Please enter word: ")
    string_list.append(word)

join_char = input("Please enter char to join strings in list: ")

result = ""

for index in range(len(string_list)):
    if index % 2 == 0:
        result = result + string_list[index] + join_char

restult = result[:-1]

print(result)'''

join_char = input("Please enter char to join strings in list: ")
result = ""

for i in range(5):
    word = input("Please enter word: ")
    if i % 2 == 0:
        result = result + word + join_char

print(result[0:-1])