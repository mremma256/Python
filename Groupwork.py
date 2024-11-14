#Qn1
coursemks = [34.4, 45, 23.9, 10.2]
total = 0
for mark in coursemks:
    total += mark
    average = total/len(coursemks)
    print(average)

#Qn2
list = [15, 42, 73, 29, 91, 50]
max = list[0]
for n in list:
    if n > max:
        max = n
print("The largest number in the list is:", max)

#Qn3
list = [12, 17, 24, 29, 36, 43, 50]
n = 0
for n in list:
    if n % 2 == 0:
        print(n)

#Qn4
while True:
 no = int(input("Enter a number: "))
 if no % 2 == 0:
  print("Number is even!")
  break

