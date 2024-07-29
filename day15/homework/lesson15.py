# homework 1:
#შექმენით ფუნქცია, რომელსაც გადასცემთ თქვენ სახელს და გვარს. გამოიყენეთ split, indexing და დაბეჭდეთ თქვენი ინიციალები. test case: input( David Tezelashvili -> output) D.T

def initial_chars(fullname):
    splited_fullname = fullname.split(" ")
    
    firstname = splited_fullname[0]
    lastname = splited_fullname[1]

    result = firstname[0] + "." + lastname[0]
    print(splited_fullname)
    
    print(result)

initial_chars("Gega Devdariani")


# homewrok 2:
#შექმენით ფუნქცია, რომელსაც გადასცემთ სიას. თქვენი დავალებაა, რომ დაბეჭდოთ ამ სიის საშუალო არითმეტიკული (ჯამი / სიგრძე)

def avreage_arithmetic(number_list):
    jami = sum(number_list)
    result = jami / len(number_list)

avreage_arithmetic([1,2,3])

'''list = [4, 9, 7, 12, 3]

length = 5
def _sum(list_to_sum):
    sum_of_list = 0
    for number in list_to_sum:
        sum_of_list += number
    return sum_of_list

function_sum = _sum(list)

def divide_(function_sum):
    print(function_sum // 5)

print(function_sum // 5)

# homewrok 3:
#შექმენით ფუნქცია, რომელსაც გადასცემთ სიტყვას და შემოწმდება არის თუ არა ის პალინდრომი (პალინდრომია სიტყვა, თუ მისი შებრუნებულიც იგივე გამოდის, მაგ: level)

word = input["enter word: "]
def palindrome(word):
    if word == word[::-1]:
     print("False")
    else: word != word[::-1]
print("True")
   





# homewrok 4:
#შექმენით ფუნქცია, რომელსაც გადასცემთ სთრინგს. თქვენი დავალებაა, რომ ამ სთრინგს მოაშოროთ ყველა სფეისი - space და დაბეჭდოთ ამ სახით test case: input) "     Goal-   Oriented   Academy    " -> output) "Goal-OrientedAcademy"

def function(string)



# homewrok 5:
#შექმენით ფუნქცია, რომელსაც გადასცემთ სიას. ამ სიაში უნდა გქონდეთ როგორც დადებითი, ასევე უარყოფითი რიცხვები. თქვენი დავალებაა, რომ გამოიტანოთ უარყოფითი რიცხვების რაოდენობა და დადებითი რიცხვების ჯამი (გამოიყენეთ for ციკლი ორივეზე)
   
list [3, 4, -9, 3, -10, -11]'''
