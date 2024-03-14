for x in range(99, 0, -1):
  if x == 1:
    print (str(x) + " bottle of beer on the wall")
    print (str(x) + " bottle of beer")
    print("Take it down, Pass it around")
    print (str(x - 1) + " bottles of beer on the wall!")
  else:
    print(str(x) + " bottles of beer on the wall")
    print (str(x) + " bottles of beer")
    print("Take one down, Pass it around")
    print (str(x - 1) + " bottles of beer on the wall")
    print(" ")
