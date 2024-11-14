#QUESTION 1
print()
Birth = int(input("Enter your year of birth: "))
Age = 2024-Birth
print(f"You are {Age} years old")
print()

#QUESTION 2
print()
A = int(input("Enter number A : "))
B = int(input("Enter number B : "))
print()
Sum = A+B
Product = A*B
print(f"Sum of these numbers is {Sum} and the product of these numbers is {Product}")
print()

#QUESTION 3
print()
Value = int(input("Enter value >> "))
print(f"Number is {Value}")
Square = Value**2
print(f"Its square is {Square}")
print()

#QUESTION 4
print()
A = int(input("Enter number A >> "))
B = int(input("Enter number B >> "))
print()
Sum = A+B
print(f"Sum of {A} and {B} is {Sum}")
Product = A*B
print(f"Product of {A} and {B} is {Product}")
print()

#QUESTION 5
print()
length  = int(input("Enter length >> "))
breadth = int(input("Enter breadth >> "))
print()
Perimeter = 2*(length+breadth)
print(f"Perimeter of Rectangle = {Perimeter}")
Area = length*breadth
print(f"Area of Rectangle = {Area}")
print()

#QUESTION 6
print()
Celsius = float(input("Enter Celsius value >> "))
F = 1.8*Celsius+32
print(f"Fahrenheit Value is {F}")
print()

#QUESTION 7
print()
R = float(input("Enter the Radius >> "))
Diameter = 2*R
print(f"Diameter = {Diameter:.0f}")
import math
Area = (math.pi * (R**2))
print(f"Area = {Area:.2f}")
Circumference = math.sqrt(Area/math.pi)*math.pi*2
print(f"Circumference: {Circumference:.2f}")
print()

#QUESTION 8
print()
Height = float(input("Enter Height >> "))
Base = float(input("Enter Base >> "))
Product = Height*Base
Area = Product/2
print(f"Area of Triangle = {Area:.2f}")
print()

#QUESTION 9
print()
Price = float(input("Enter Price >> "))
VAT = (18/100)*Price
print(f"VAT is : {VAT:.2f}")
VAT_price = Price+VAT
print(f"VAT price is : {VAT_price:.2f}")
print()

#QUESTION 10
print()
A = int(input("Enter Side A >> "))
B = int(input("Enter Side B >> "))
length = (A**2 + B**2)**0.5
print(f"Hypotenuse = {length:.0f}")
print()

#QUESTION 11
print()
initial_reading = int(input("Enter initial reading: "))
Final_reading = int(input("Enter final reading: "))
Consumption = Final_reading-initial_reading
print(f"Consumption = {Consumption} L")
Cost = 1.50*Consumption
print(f"Cost        = Shs {Cost:.2f}")
print()

#QUESTION 12
print()
initial_km = int(input("Enter initial km: "))
Final_km = int(input("Enter final km: "))
Fuel_in_litres = int(input("Enter fuel in litres: "))
print()
Distance = Final_km-initial_km 
print(f"Distance = {Distance} km")
Consumption = Distance/Fuel_in_litres
print(f"Consumption =  {Consumption:.0f} km / litre")
print()

#QUESTION 14
print()
print("Population Figures")
print("==================")
print()
Current_stand = 43000000
Percentage = 12.3
year_1 = ((12.3/100)*Current_stand)+Current_stand
print(f"2025 = {year_1:.0f}")
year_2 = ((12.3/100)*year_1)+year_1
print(f"2026 = {year_2:.0f}")
year_3 = ((12.3/100)*year_2)+year_2
print(f"2027 = {year_3:.0f}")
print()

#QUESTION 15
print()
x1 = int(input("Enter 1st x-coordinate >> "))
y1 = int(input("Enter 1st y-coordinate >> "))
print()
x2 = int(input("Enter 2nd x-coordinate >> "))
y2 = int(input("Enter 2nd y-coordinate >> "))
x = 1/2*(x1+x2)
y = 1/2*(y1+y2)
print()
print(f"Midpoint is at ({x} ; {y})")
print()

#QUESTION 16
print()
x1 = int(input("Enter 1st x-coordinate >> "))
y1 = int(input("Enter 1st y-coordinate >> "))
print()
x2 = int(input("Enter 2nd x-coordinate >> "))
y2 = int(input("Enter 2nd y-coordinate >> "))
print()
Gradient = (y2-y1)/(x2-x1)
print(f"Gradient is: {Gradient}")
print()

#QUESTION 17
print()
import math
x = 5
x_1 =3
N = (((x**4)-(x**3))+((x**2)-x))/((x+1)**2-(math.sqrt(x)))
print(f"N = {N:.5f}")
N_1 = (((x_1**4)-(x_1**3))+((x_1**2)-x_1))/((x_1+1)**2-(math.sqrt(x_1)))
print(f"N = {N_1:.6f}")
print()

#QUESTION 18
print()
mark = int(input("Enter mark           : "))
original_total = int(input("Enter original total : "))
Enter_new_total = int(input("Enter new total      : "))
Converted_Mark = (mark/original_total)*Enter_new_total
print()
print(f"Converted Mark = {Converted_Mark:.0f}")
print()

#QUESTION 22
print()
import math
Seconds = int(input("Enter Value in Seconds >> "))
Hr = 60
Mn = 60
sec = 60
count_hours = math.floor(Seconds/(Mn*day))
count_minutes = math.floor(Seconds/Mn)
count_seconds = math.floor(Seconds-(count_minutes*sec))
print(f"Hours =  Minutes = {count_minutes} Seconds = {count_seconds}")
print()

#QUESTION 23
print()
import math
Minutes = int(input("Enter Value in Minutes >> "))
day = 24
Hr = 60
count_days = math.floor(Minutes/(Hr*day))
count_hrs = math.floor((Minutes-(count_days*day)*Hr)/Hr)
count_minutes = math.floor((Minutes-(count_days*day)*Hr)-(count_hrs*Hr))
print(f"Days = {count_days} Hours = {count_hrs} Minutes = {count_minutes}")
print()

#QUESTION 24
print()
import math
Number = int(input("Enter Number of Pupils >> "))
Ratio = 1;5
Number_teachers = math.floor(Number/5)
print(f"The school may have {Number_teachers} teachers.")
print()

#QUESTION 25
print()
import math
Number_1 = int(input("Enter 1st Number >> "))
Number_2 = int(input("Enter 2st Number >> "))
print()
divide = Number_2/Number_1
count = math.floor(divide)
Remainder = Number_2%Number_1
print(f"{Number_1} divides into {Number_2} {count} times with a remainder of {Remainder:.0f}.")
print()