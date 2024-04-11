




'''name = "luka"
print(name.capitalize())
print(name.lower())
print(name.upper())

name1 = "Lile"

print(name1.find("L"))'''

def my_find(collection, value_to_find):

    for index in range(len(collection)):
        if collection[index] == value_to_find:
            return index
        
print(my_find(["luka", "lile", "nia"], "lile"))  



#range - დიაპაზონი სიაში(რიცხვთა შორის)
#len - გვეუბნება რამდენი ელემენტია სიაში
