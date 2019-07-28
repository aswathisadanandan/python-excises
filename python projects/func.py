a=int(input("Enter a value"))
b=int(input("Enter the limit"))
c=10
def mult(a,b):
  c=5
  print(c)
  n=range(1,b+1)
  for i in n:
    print(i,"*",a,"=",(i*a))
mult(a,b)
print(c)
