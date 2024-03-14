# Write code below 💖

gryffindor = 0
ravenclaw = 0
slytherin = 0
hufflepuff = 0

print("Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
q1 = int(input())

if q1 == 1:
  gryffindor += 1
  ravenclaw += 1
elif q1 == 2:
  slytherin += 1 
  hufflepuff += 1
else:
  print("gtfo")

print("When I'm dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")

q2 = int(input())

if q2 == 1:
  hufflepuff += 2
elif q2 == 2:
  slytherin += 2
elif q2 == 3:
  ravenclaw += 2
elif q2 == 4:
  gryffindor += 2
else:
  print("gtfo")

print ("Which kind of instrument most pleases your ear?")
print ("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
q3 = int(input())

if q3 == 1:
  slytherin += 4
elif q3 ==2: 
  hufflepuff += 4
elif q3 == 3:
  ravenclaw += 4
elif q3 == 4:
  gryffindor += 4
else:
  print("gtfo")

print("Now let us see...")
if hufflepuff >= 4:
  print("HUFFLEPUFF!")
elif ravenclaw >= 4:
  print("RAVENCLAW!")
elif slytherin >= 4:
  print("SLYTHERIN!")
elif gryffindor >= 4:
  print("GRYFFINDOR!")

