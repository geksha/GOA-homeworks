person = {
    # key    value
    "name": "davit",
    "surname": "Grdzelishvili",
    "age": "20",
    "arr": [1,2,3,4,5,6]
}

# შეგვიძლია შევუცვალოთ მნიშვნელობები
person['name'] = "George"
# update შეუძლია შეცვალოს და დაამატოს ახალი აითემები თავისი value-ბით
person.update({"name": "Daviti"})
person.update({"car": "Aston Martin "})

print(person)



# გვიბრუნებს value
print(person["name"], "/ arr method")
# გვიბრუნებს value
print(person.get('name'), '/ get method')

#----------------------
print(person.values(), "valuessssss")
#----------------------

#----------------------
# გვიბრუნებს key
x = person.keys()
print(person.keys())
#----------------------

#----------------------
# აბრუნებს წყვილ tuples
print(person.items(), "items   ")
#----------------------

# გვიბრუნებს key
print(person["arr"][0])
print(len(person))
      
x = person["arr"]
print(x)

# item-ის დამატება
person['food'] = "mtsvadi"



person.pop("car")
person.popitem()
del person['name']
# del person
person.clear()
print(person)
