#მომხმარებელს შემოატანინეთ სახელი, შემდეგ კი გვარი. შეინახეთ ისინი სიაში და წინა დავალების მსგავსად იმუშავეთ ყველა ელემენტზე capitalize მეთოდით. თქვენი დავალებაა, რომ გამოიტანოთ მომხმარებლის ინიციალები სთრინგის სახით. test case: input) "Data", "Tezelashvili" -> output: "D.T"

firstname = input("Please enter your firstname: ").capitalize()
lastname = input("Please enter lastname: ")

result = firstname[0] + ',' + lastname[0]

print(result)
 
