#შექმენით ოთხი მათემატიკური ფუნქცია, თითოეულს გადაეცით ორი არგუმენტი და სახელის შესაბამისად მოახდინეთ მუშაობა. ოპერაციები: +, -, *, /

# pirveli

def plus_(num1, num2):
    print(num1 + num2)

plus_(15, 20)


def minus_(num1, num2):
    print(num1 - num2)

minus_(50, 28)


def divide_(num1, num2):
    print(num1 // num2)

divide_(75, 15)

def multiplication_(num1, num2):
    print(num1 * num2)

multiplication_(200, 20)



#დავალება2: შექმენით ფუნქცია, რომელსაც გადასცემთ მართკუთხედის სიგრძესა და სიმაღლეს, გამოითვლით მის ფართობს

# meore

def length_and_height(num1, num2):
    print(num1 * num2)

length_and_height(10, 15)



#დავალება3: შექმენით ფუნქცია, რომელსაც გადასცემთ მართკუთხედის ოთხ გვერდს, გამოითვლით მის პერიმეტრს

# mesame

def pages(num1, num2):
    print(2 * (num1 + num2))

pages(10, 12)



#დავალება4: შექმენით ფუნქცია, რომელიც მიიღებს არგუმენტად სიას და დაბეჭდეთ სიის რიცხვების ჯამი, არ გამოიყენოთ sum

# meotxe
 
#list = [10, 12, 14, 9, 7]

# pirveli xerxi (arachaduri)
#list_sum = sum(list)

#print("list_sum:", list_sum)


# meore xerxi (pirvelze uketesi)

#manual_sum = 0

#for number in list: 
#    manual_sum += number

#print("manual_sum:", manual_sum)


#mesame xerxi (chaduri)

list = [10, 12, 14, 9, 7]

def _sum(list_to_sum):
    sum_of_list = 0
    for number in list_to_sum:
        sum_of_list += number
    return sum_of_list

function_sum = _sum(list)

print("sum_list:", function_sum)



#დავალება5: შექმენით ფუნქცია, რომელიც დაბეჭდავს კონკრეტული სიიდან მინიმალურ და მაქსიმალურ რიცხვებს, არ გამოიყენოთ min და max. გამოიყენეთ def, for, if/else, indexing, print

# mexute

# max numberis dabewdva

list1 = [3, 19, 10, 17, 26]

def find_max(list1):

  max = list1[0]

  for number in list1:
    if (number > max):
      max = number


  return max   

max = find_max(list1)

print("Max number:", max)


# min numberis dabewdva 

def find_min(list1):
   
  min = list1[0]

  for number in list1:
    if (number < min):
      min = number

  return min

min = find_min(list1)

print("Min number", min)


# end of classwork.

