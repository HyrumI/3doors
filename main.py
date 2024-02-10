
#Define variables
import random
money = random.randint(1,3)
Door1 = 0
Door2 = 0
Door3 = 0
emptyDoor = 0
if money == 1:
  Door1 = 1
elif money == 2:
  Door2 = 1
elif money == 3:
  Door3 = 1

#Create graphics
def closedDoors():
  print("   I=============I  I=============I  I=============I   ")
  print("   |             |  |             |  |             |   ")
  print("   |   Door  1   |  |   Door  2   |  |   Door  3   |   ")
  print("   |             |  |             |  |             |   ")
  print("   |             |  |             |  |             |   ")
  print("   |             |  |             |  |             |   ")
  print("   |           0 |  |           0 |  |           0 |   ")
  print("   |             |  |             |  |             |   ")
  print("   |             |  |             |  |             |   ")
  print("   |             |  |             |  |             |   ")
  print("   |             |  |             |  |             |   ")
  print("   |             |  |             |  |             |   ")
  print("   I=============I  I=============I  I=============I   ")
def emptyDoorOne():
  print("   I=============I  I=============I  I=============I   ")
  print("   |\           /|  |             |  |             |   ")
  print("   | \ Door  1 / |  |   Door  2   |  |   Door  3   |   ")
  print("   |  \       /  |  |             |  |             |   ")
  print("   |   \     /   |  |             |  |             |   ")
  print("   |    \   /    |  |             |  |             |   ")
  print("   |      X    0 |  |           0 |  |           0 |   ")
  print("   |    /   \    |  |             |  |             |   ")
  print("   |   /     \   |  |             |  |             |   ")
  print("   |  /       \  |  |             |  |             |   ")
  print("   | /         \ |  |             |  |             |   ")
  print("   |/           \|  |             |  |             |   ")
  print("   I=============I  I=============I  I=============I   ")
def emptyDoorTwo():
  print("   I=============I  I=============I  I=============I   ")
  print("   |             |  |\           /|  |             |   ")
  print("   |   Door  1   |  | \ Door  2 / |  |   Door  3   |   ")
  print("   |             |  |  \       /  |  |             |   ")
  print("   |             |  |   \     /   |  |             |   ")
  print("   |             |  |    \   /    |  |             |   ")
  print("   |           0 |  |      X    0 |  |           0 |   ")
  print("   |             |  |    /   \    |  |             |   ")
  print("   |             |  |   /     \   |  |             |   ")
  print("   |             |  |  /       \  |  |             |   ")
  print("   |             |  | /         \ |  |             |   ")
  print("   |             |  |/           \|  |             |   ")
  print("   I=============I  I=============I  I=============I   ")
def emptyDoorThree():
  print("   I=============I  I=============I  I=============I   ")
  print("   |             |  |             |  |\           /|   ")
  print("   |   Door  1   |  |   Door  2   |  | \  Door  3/ |   ")
  print("   |             |  |             |  |  \       /  |   ")
  print("   |             |  |             |  |   \     /   |   ")
  print("   |             |  |             |  |    \   /    |   ")
  print("   |           0 |  |           0 |  |      X    0 |   ")
  print("   |             |  |             |  |    /   \    |   ")
  print("   |             |  |             |  |   /     \   |   ")
  print("   |             |  |             |  |  /       \  |   ")
  print("   |             |  |             |  | /         \ |   ")
  print("   |             |  |             |  |/           \|   ")
  print("   I=============I  I=============I  I=============I   ")
def openDoorOne():
  print("   I=============I  I=============I  I=============I   ")
  print("   |           |||  |             |  |             |   ")
  print("   |           |||  |   Door  2   |  |   Door  3   |   ")
  print("   |           |||  |             |  |             |   ")
  print("   |           |||  |             |  |             |   ")
  print("   |   _____   |||  |             |  |             |   ")
  print("   |   \\ //   |||  |           0 |  |           0 |   ")
  print("   |   /===\   |||  |             |  |             |   ")
  print("   |  /     \  |||  |             |  |             |   ")
  print("   | |  $$$  | |||  |             |  |             |   ")
  print("   |  \_____/  |||  |             |  |             |   ")
  print("   |           |||  |             |  |             |   ")
  print("   I=============I  I=============I  I=============I   ")
def openDoorTwo():
  print("   I=============I  I=============I  I=============I   ")
  print("   |             |  |           |||  |             |   ")
  print("   |   Door  1   |  |           |||  |   Door  3   |   ")
  print("   |             |  |           |||  |             |   ")
  print("   |             |  |           |||  |             |   ")
  print("   |             |  |   _____   |||  |             |   ")
  print("   |           0 |  |   \\ //   |||  |           0 |   ")
  print("   |             |  |   /===\   |||  |             |   ")
  print("   |             |  |  /     \  |||  |             |   ")
  print("   |             |  | |  $$$  | |||  |             |   ")
  print("   |             |  |  \_____/  |||  |             |   ")
  print("   |             |  |           |||  |             |   ")
  print("   I=============I  I=============I  I=============I   ")
def openDoorThree():
  print("   I=============I  I=============I  I=============I   ")
  print("   |             |  |             |  |           |||   ")
  print("   |   Door  1   |  |   Door  2   |  |           |||   ")
  print("   |             |  |             |  |           |||   ")
  print("   |             |  |             |  |           |||   ")
  print("   |             |  |             |  |   _____   |||   ")
  print("   |           0 |  |           0 |  |   \\ //   |||   ")
  print("   |             |  |             |  |   /===\   |||   ")
  print("   |             |  |             |  |  /     \  |||   ")
  print("   |             |  |             |  | |  $$$  | |||   ")
  print("   |             |  |             |  |  \_____/  |||   ")
  print("   |             |  |             |  |           |||   ")
  print("   I=============I  I=============I  I=============I   ")

#Door selection
closedDoors()
print("")
print("Behind one of these doors is $1,000,000 if you can pick the correct door it's yours.")
while True:
  try:
    DoorPick = int(input("Please choose a door. (1, 2, or 3) : "))
    if DoorPick == 1 or DoorPick == 2 or DoorPick == 3:
      print("You have selected door", DoorPick)
      break
    else:
      print("Please press the 1, 2, or 3 key then hit enter to select a door.")
      print("")
  except:
    print("Please press the 1, 2, or 3 key then hit enter to select a door.")
    print("")

#Show empty door
print("")
print("Now for the twist.")
if money == DoorPick:
  if money == 1:
    emptyDoor = random.randint(2,3)
  elif money == 2:
    while True:
      emptyDoor = random.randint(1,3)
      if money == 1 or 3:
        break   
  elif money == 3:
    emptyDoor = random.randint(1,2)
  if emptyDoor == 1:
    emptyDoorOne()
  elif emptyDoor == 2:
    emptyDoorTwo()
  elif emptyDoor == 3:
    emptyDoorThree()
  print("Door", emptyDoor, " was empty.")
else:
  if DoorPick == 1:
    if money == 2:
      emptyDoor = 3
      emptyDoorThree()
      print("Door 3 was empty.")
    else:
      emptyDoor = 2
      emptyDoorTwo()
      print("Door 2 was empty.")
  elif DoorPick == 2:
    if money == 1:
      emptyDoor = 3
      emptyDoorThree()
      print("Door 3 was empty.")
    else:
      emptyDoor = 1
      emptyDoorOne()
      print("Door 1 was empty.")
  elif DoorPick == 3:
    if money == 1:
      emptyDoor = 2
      emptyDoorTwo()
      print("Door 2 was empty.")
    else:
      emptyDoor = 1
      emptyDoorOne()
      print("Door 1 was empty.")

#Offer a switch
print("")
print("Now that you have learned this new information I'll offer you another choice.")
while True:
  switch = input("Would you like to switch doors? (Type Y or N)").lower()
  if switch == "y":
    if DoorPick == 1:
      if emptyDoor == 2:
        DoorPick = 3
      elif emptyDoor == 3:
        DoorPick = 2
      print(DoorPick)
    elif DoorPick == 2:
      if emptyDoor == 1:
        DoorPick = 3
      elif emptyDoor == 3:
        DoorPick = 1
      print(DoorPick)
    elif DoorPick == 3:
      if emptyDoor == 2:
        DoorPick = 1
      elif emptyDoor == 1:
        DoorPick = 2
    print("Door was switched to Door", DoorPick)
    break
  elif switch == "n":
    print("Door was not switched and is still Door", DoorPick)
    break
  else:
    print("Please type Y for yes and N for no.")

#Show me the money
print("")
print("Now lets see if you won.")
print("The money was behind door", money)
if money == 1:
  openDoorOne()
elif money == 2:
  openDoorTwo
elif money == 3:
  openDoorThree()

#Did they win
if money == DoorPick:
  print("You just won $1,000,000!!!")
else:
  print("It looks like today just isn't your day maybe next time.")