from pokemon_defn.charmander import charmander
from pokemon_defn.squirtle import squirtle
from pokemon_defn.bulbasaur import bulbasaur
from class_defn.trainer import Trainer
from items.potions import regular_potion
from utils import slow_print, show_pokemon_table

name = input("\nEnter your name: ")
slow_print("\nHey " + name + "! Let's get started, go ahead and choose your first Pokemon!")

show_pokemon_table((charmander, squirtle, bulbasaur), False)

while (True):
    slow_print("\nEnter\n 1. for Charmander\n 2. for Squirtle\n 3. for Bulbasaur")
    try:
        starter_pokemon_choice = int(input("\nEnter here: "))
    except:
        slow_print("\nInvalid. Try again.")
        continue

    if (starter_pokemon_choice == 1):
        player = Trainer(name, [charmander], [])
        misty = Trainer("Misty", [bulbasaur], [])
        break
    elif (starter_pokemon_choice == 2):
        player = Trainer(name, [squirtle], [])
        misty = Trainer("Misty", [charmander], [])
        break
    elif (starter_pokemon_choice == 3):
        player = Trainer(name, [bulbasaur], [])
        misty = Trainer("Misty", [squirtle], [])
        break
    else:
        slow_print("\nInvalid. Try again.")

slow_print("\nGreat choice! Let's start your Pokemon journey!")
slow_print("\nNo better way to start than with a battle! Let's go!")

result_won = False
while (not result_won):
    result_won = player.battle(misty)
    if (not result_won):
        slow_print("\nAh that's a shame! Try again.")
        player.team[0].full_heal()

slow_print("\nYou won! Congratulations!")
player.receive_item(regular_potion)
slow_print("Use it wisely.")

while(True):
    slow_print("\n What's next?\n1. My team \n2. Inventory \n3. Exit")
    try:
        choice = int(input("Enter here: "))
    except:
        slow_print("\nInvalid. Try again.")
        continue
    if (choice == 1):
        player.show_team()
    elif (choice == 2):
        player.show_inventory()
    elif (choice == 3):
        slow_print("\nFarewell, Trainer. Until next time.")
        break
    else:
        slow_print("\nInvalid. Try again.")
