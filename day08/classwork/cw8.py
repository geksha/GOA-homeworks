age = int(input("whats your age? :"))

if age >= 0 and age < 13:
    print("you are kid")
elif age >= 13 and age < 18:
    print("you are teenager")
elif age >= 18 and age < 60:
    print("you are an adult")
else:
    print("you are old")