from Vehicle import *

v1 = Vehicle("Chris",100,"N")
v2 = Vehicle("Jordan",200,"S")


v1.print_info()
v2.print_info()

v1.speed = 400
v1.direction = "S"
v2.drection = "N"
v2.speed = 500

print("Updated Vehicles:")

v1.print_info()
v2.print_info()



print("------------------------------------- Cars")
v3 = Car("Patrick",100,"W",15,0,20)
v3.print_info()
print("\n")
v3.xyz()
print("\n")
v3.drive(102)
v3.print_info()
print("\n")
v3.fill_up(2)
v3.print_info()