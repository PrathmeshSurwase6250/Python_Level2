name = "Prathmesh surwase" 
print(len(name))
print(name.center(50).upper())
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.replace('s' , "S"))
print(name.find("a"))
print(name.isalpha())
print(name.rstrip("~"))
print(name[1:9])


student = ["Prathamesh", 22, 8.2, True]

print(student)
student.append(23)
print(student.pop())
print(student.count(22))
print(student.index(8.2))
student.reverse()
print(student)

def add (a): 
    '''This is an doc function'''

print(add.__doc__)

print(f"the list is {student}")