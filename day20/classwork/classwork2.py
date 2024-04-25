#გადმოგეცემათ სია რომელშიც იქნება რიცხვები int ტიპის მონაცემები. 
#დააბრუნეთ ახალი სია მაგრამ ამ სიაში უნდა იყოს მხოლოდ ლუწი რიცხვები და დაპრინტეთ ახალი სია

'''list = [7, 4, 5, 6, 3, 10]
new_list = []

def summ(listn):
    for i in listn:
        if i % 2 == 0:
            new_list.append(i)
        else:
            list.append(i)
    sum_even = sum(new_list)
    sum_odd = sum(list)
    return [listn]'''



'''my_list = [2,5,1,313,63,123,5234]
new_list = []

for num in my_list:
  if num % 2 == 0:
    new_list.append(num)
print(new_list)'''

'''my_list = [2,5,1,313,63,123,5234]
even_list = []
odd_list= []

for num in my_list:
  if num % 2 == 0:
    even_list.append(num)
else:
    odd_list.append(num)

print(even_list,odd_list)'''

my_list = [2,5,1,313,63,123,5234]
even_list = []
odd_list= []

for i in range(len(my_list)):
  if i % 2 == 0:
    even_list.append(my_list[i])
  else:
    odd_list.append(my_list[i])

print(even_list,odd_list)



    
    

