# Zack Garzella
# Cube surface area
# This program finds the surface area of a cube with the edge length given...
#...by the user

edge_len = input("Enter the edge length of a cube: ")
edge_len = int(edge_len)

cube_area = (edge_len ** 3)
cube_area = int(cube_area)
cube_area_str = str(cube_area)

print("The surface area of this cube is", cube_area_str)

input("\n\nPress enter key to exit")
