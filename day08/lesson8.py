name = input("Please enter your name: ")
password = input("Please enter your password: ")
repeat_password = input("Please repeat your password: ")

if repeat_password:
    print(name, "password is correct, welcome")
else:
    print("password does not match")


