#მომხმარებელს შემოატანინეთ სიტყვა. თქვენი დავალებაა, რომ ლუწ ინდექსებზე მყოფი ასოები გარდაქმნათ uppercase-ად, ხოლო კენტ ინდექსებზე მყოფები lowecase-ად, საბოლოოდ კი დაბეჭდოთ შედეგი.
#len - რამდენი ელემენტია ცვლადში

user_word = input("Please enter uppercase word: ")

for index in range(len(user_word)):
    if index % 2 == 0:   
        result = result + user_word[index].upper()
    else: 
        result = result + user_word[index].lower()

print(result)    
