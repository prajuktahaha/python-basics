student = {
    "name" : "Prajukta Harichandan",
    "subject" : {
        "phy" : 85,
        "chem" :90,
        "math" :70,
    }
}

print(student.keys())
#forlength
print(len(list(student.keys())))
#forvalues
print(student.values())
#forconvertintolist
print(list(student.values()))
#foritems
print(student.items())
#convertintolist
print(list(student.items()))
#forindividuallist
pairs = list(student.items())
print(pairs[0])
print(pairs[1])
#for"get"methods
print(student.get("name")) #but if i type print(student.get("name2")) it will return None
#for"update"methods
new_dict = {"city": "Bhubaneswar"}
new_dict = {"age": "20"}

student.update(new_dict)
