num = input("Enter a number:")
thislist = []
for i in range(1, num + 1):
  if num % i == 0:
    thislist.append(i)
print("The factors of " + str(num) + " is " + str(thislist)
for x in thislist:
  print(x)
