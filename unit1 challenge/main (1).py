
y=int(input("Enter the year:"))
if(y%400==0) and (y%100==0):
  print(y,"is the leap year")
elif(y%4==0) and (y%100!=0):
  print(y,"is the leap year")
else:
  print(y,"is not the leap year")