# Just a little choose-your-own adventure that works on nested if/else statements.

forest_choice = input("You wake up in a strange forest.\nTo your right you see more woods and a strange fog.\nTo your left you hear the sound of water washing against the shore.\nDo you choose 'left' or 'right'?\n")
if forest_choice.lower() == "left":
  swim_choice = input("You stand at the shore and in the distance see a small island in the lake.\nYou see a faint blue glow and feel it calling to you.\nDo you 'wait' or try and 'swim' out to the island?\n")
  if swim_choice.lower() == "wait":
    door_choice = input("You come across three doors deep in the woods, do you choose the 'red', 'blue', or 'yellow' door to enter?\n")
    if door_choice.lower() == "yellow":
      print("You have found the treasure")
    elif door_choice.lower() == "red":
      print("Fire bursts through the door and leaves you as chared dust.")
    else:
      print("A torrent of water endlessly streams forward and engulfs you. The water enters your lungs and darkness creeps in as you gasp for air.")
  else:
    print("As you swim into the water a chill begins to sap your strength. Half way to your destination the energy leaves your body and you drown in the lake.")
else:
  print("You wander into the woods and are never seen or heard from again.")
  