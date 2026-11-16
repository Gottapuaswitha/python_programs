'''student = {101: ("Aswitha", "CSE", 2026, 3, "A"),102:["Sireesha","CSE",2025,4,"B"]}
print(student)

#roll_number=int(input("enter your roll number:"))
#print(student.get(roll_number),"not available")

names=list(student.values())
print(names[0][0])
print(len(student.keys()))'''
l = [
    {"name": "hari", "age": 22, "group": "cse"},
    {"name": "dinesh", "age": 24, "group": "ece"}
]
'''
print(l)

##particular age access

print(l[1]["age"])

##Name access

print(l[0]["name"])

print(l[0].keys())

print(l[0].values())

print(l[0].items())
l.append({"name": "ramya", "group": "cse"})

print(l)
l.insert(1, {"name": "sita", "age": 23, "group": "mec"})

print(l)
l[0].update({"city": "Hyderabad"})

print(l)
l[0]["age"] = 25

print(l)
'''


