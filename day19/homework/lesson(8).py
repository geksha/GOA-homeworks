#თქვენი დავალებაა, რომ შექმნათ იგივე ლოგიკა რაც წინა დავალებაში გქონდათ, უბრალოდ find მეთოდის გარეშე - გამოიყენეთ ციკლი. საბოლოოდ შეამოწმეთ ორივე ალგორითმის მუშაობა და შეამოწმეთ იგივე შედეგებს თუ მიიღებთ.

def manual_find(collection, find_item):
    for index in range(len(collection)):
        if collection[index] == find_item:
            return index
    return -1

print(manual_find("Luka", "x"))