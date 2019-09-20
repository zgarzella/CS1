# Zack Garzella
# Cylinder Program
# This program finds the area and volume of a cylinder with the user's input...
#... of the radius and length

radius = float(input("Please enter the radius of your cylinder: "))
length = float(input("Please enter the length of your cylinder: "))
pi = float(3.14159)

volume = float(radius ** 2 * length * pi)
surface_area = float((radius ** 2 * pi * 2) + (2 * pi * radius * length))

print("The volume of your cylinder is", volume)
print("The surface area of your cylinder is", surface_area)

input("\n\nPress enter key to exit")
