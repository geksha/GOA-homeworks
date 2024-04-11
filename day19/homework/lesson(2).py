#მომხმარებელს შემოატანინეთ სიტყვა. for ციკლის გამოყენებით შეამოწმეთ მისი თითოეული ასო და თუ რომელიმე იქნება lowercase, მაშინ მომხმარებელს შემოატანინეთ სიტყვა თავიდან. ასევე დაბეჭდეთ თუ რამდენჯერ მოუწია მომხმარებელს სიტყვის შემოტანა - counter.
#char - სიმბოლო
user_word = input("Please enter uppercase word: ")

count = 1

for char in user_word:
    
    if char.lower() not in user_word:
        user_word = input("Please enter uppercase word: ")
        count = count + 1
         
print(count, user_word)





