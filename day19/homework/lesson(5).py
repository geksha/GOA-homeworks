#სიაში შეინახეთ თქვენი სახელი და გვარი. capitalize მეთოდის გამოყენებით მასივის ყველა ელემენტზე მოახდინეთ მუშაობა და ბოლოს დაბეჭდეთ უკვე შეცვლილი სია.

names = ["luka", "gio", "lile", "nia"]

for index in range(len(names)):
    names[index] = names[index].capitalize()

print(names)
