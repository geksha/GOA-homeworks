# დავალება: უნდა გამოვიტანოთ ყველა სიმბოლო იმაზე 1-ხელ მეტჯერ რა ინდექსიც აქვს, უნდა შევაერთოთ დეფისებით დ ასევე ყველა უნდა იყოს capitalized

# 1 გზა

def accum(s):
    return "-".join([s[i].upper() + (s[i].lower() * i) for i in range(len(s))])

# 2 გზა

# "abcd" - ["A", "Bb", "Ccc", "Dddd"]

# 1. შევქმნათ ცარიელი list-ი
# 2. უნდა შევქმნათ for loop
# 3. მიღებული შედეგი უნდა დავა-append-ოთ ცარიელ ლისტში
# 4. გამოვიყენოთ return, გამოვიყენოთ join და მივცეთ არგუმენტად "-".

def accum(st):
    listn = [] #result

    for i in range(1, len(st) + 1):
        listn.append((st[i - 1] * i).capitalize())
 
    return "-".join(listn)

st = "abcd"

# for i in st:
#     print(i)

# for i in range(1, len(st) + 1):
#     print(i)

# print("A" * 10)

# 10 * 2 = 10 + 10
# 