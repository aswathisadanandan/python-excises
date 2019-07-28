n=range(25,100)
for y in n:
  x=range(2,y)
  for i in x:
    if y % i == 0:
      break
  else:
    print(y)

