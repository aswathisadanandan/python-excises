person=dict(Name="Aswathi",Age=20,Salary=6000)
print(person)
print(person["Name"])
person["Name"]="Adarsh"
print(person["Name"])
person["Insur"]="yes"
print(person)
del person["Age"]
print(person)
person=dict(Name="Aswathi",Age=20,Salary=6000)
print(person.get("Age", 10))


