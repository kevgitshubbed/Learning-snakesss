

# Introduction Menu
print("Which shape should we calculate the area of?")
print("1) Square")
print("2) Rectangle")
print("3) Triangle")
print("4) Circle")
print("5) Quit")
print(" ")
shape = str(input("Please enter your selection: "))
# Invalid Response Thingy
while shape != "1" and shape != "2" and shape != "3" and shape != "4" and shape != "5": 
  print("Hmmmm, please try again")
  shape = str(input("Please enter your selection: "))
  if shape == "1" or shape == "2" or shape == "3" or shape == "4":
    break
#Quit Button
if shape == "5":
  print("Going to sleep now...")
#Calculator 
elif shape == "1":
  sqrlength = float(input("What is the length of the square? "))
  sqrwidth = float(input("What is the width of the square? "))
  print("Calculating...")
  print (str(sqrlength * sqrwidth) + " is the area of the square!") 
elif shape == "2":
  rctlength = float(input("What is the length of the rectangle? "))
  rctwidth = float(input("What is the width of the rectangle? "))
  if rctlength == rctwidth:
    print("Hmmm this looks like a square, but okay...")
  print("Calculating...")
  print (str(rctlength * rctwidth) + " is the area of the rectangle!") 
elif shape == "3":
  tribase = float(input("What is the length of the triangle's base? "))
  triheight = float(input("What is the height of the triangle? "))
  print("Calculating...")
  print (str((tribase * triheight)/2) + " is the area of the triangle!") 
elif shape == "4":
  radius = float(input("What is the radius of the circle? "))
  print("Calculating...")
  print (str(3.1416 * (radius ** 2)) + " is the area of the circle!")

