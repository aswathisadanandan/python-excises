a=int(input("Enter a value"))
am=0
num=a
while a>0:
  re=a%10  
  am=(re**3)+am
  a=a//10
print(a)
print(am)
if(am==num):
  print("This number is amstrong")
else:
  print("Not an amstrong")
