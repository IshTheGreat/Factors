num = input("Enter a number:")
thislist = []
for i in range(1, num + 1):
  if num % i == 0:
    thislist.append(i)
print("The factors of " + str(num) + " is " + str(thislist)
for x in thislist:
  print(x)
if len(thislist) == 2:
      print("Your number is prime!")
elif len(thislist) > 2:
      print("Your number is composite!)
x = len(thislist)
print(str(num) + " has " + str(x) + " factors."
         
 
