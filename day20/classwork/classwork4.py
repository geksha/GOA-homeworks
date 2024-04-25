#გადმოგეცემათ რიცხვების სია, თქვენ უნდა ამოშალოთ ამ სიიდან ყველა კენტი რიცხვი და დატოვოთ მხოლოდ ლუწი რიცხვები შემდეგ კი დაბეჭდოთ

'''list = [5,9,4,8,10,11]
even_list = []
odd_list = []

for i in range(len(list)):
  if i % 2 == 0:
    even_list.pop(list)
  else:
    odd_list.append(list)

print(even_list)'''

my_list = [5,9,4,8,10,11]
#my_list.pop(2)
#print(my_list.pop(2))


for i in range(len(my_list)):
     # if my_list[i] % 2 != 0:
       # my_list.pop(i)
       # print(my_list[i])
       # print(i, "mate")
    my_list.pop(i)
print(my_list)


