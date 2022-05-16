import numpy as np
import os
print("What would you like to calculate:")
print("1. Dot Product")
print("2. Angle")
menu = int(input(">>>"))
os.system("clear")

a = input("Type in vector A from the top to the bottom leaving spaces between each number\n>")
b = input("Do the same for vector B/n>")
os.system("clear")
while len(a.split()) != len(b.split()):
        print("Both vectors must be the same length!")
        a = input("Type in vector 'a' from the top to the bottom leaving spaces between each number\n>")
        b = input("Do the same for vector b/n>")

a = np.array(list(map(int, a.split())))
b = np.array(list(map(int, b.split())))

if menu == 1:
	print("The dot product is", str(a @ b))
elif menu == 2:
	print("Are these vectors the directional and/or normal vectors of a:")
	print("1. line and a line")
	print("2. plane and a line")
	print("or")
	print("3. plane and a plane")
	choice = int(input(">>>"))
	if choice == 1:
		print("The angle between the 2 lines are", str( np.arccos( (a @ b) / ( (sum([x**2 for x in a]) ** 0.5) * (sum([x**2 for x in b]) ** 0.5) ) ) ), "in Radians")
	elif choice == 2:
		print("The angle between the plane and the line is", str( np.arcsin( (a @ b) / ( (sum([x**2 for x in a]) ** 0.5) * (sum([x**2 for x in b]) ** 0.5) ) ) ), "in Radians")
	else:
		pass
