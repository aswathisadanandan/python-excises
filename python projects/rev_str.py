str=input("Enter a string")
pali=str
str=list(str)
l=(len(str))
temp=[]
n=range(0,len(str))
for i in n :
  m=l-i
  k=m-1
  temp.append(str[k])
print(temp)

