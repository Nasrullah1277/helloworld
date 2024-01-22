x=int(input( "enter the value of angle 1 : "))
y=int(input(" enter the value of angle 2 :  "))
z=int(input(" enter the value of angle 3 : "))

if x == y == z:
   print( "Equilateral triangle" )
elif x==y or y==z or z==x:
   print("Isosceles triangle")
else:
   print("Scalene Traingle")
 