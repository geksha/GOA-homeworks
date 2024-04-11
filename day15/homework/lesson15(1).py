def initial_chars(fullname):
    splited_fullname = fullname.split(" ")
    
    firstname = splited_fullname[0]
    lastname = splited_fullname[1]

    result = firstname[0] + "." + lastname[0]
    print(splited_fullname)
    
    print(result)

initial_chars("Gega Devdariani")
