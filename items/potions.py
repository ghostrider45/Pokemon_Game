from class_defn.item import Item

regular_potion = Item("Regular Potion", "Healing", lambda target: target.heal(50), "Heals 50 HP")

super_potion = Item("Super Potion", "Healing", lambda target: target.heal(100), "Heals 100 HP")

hyper_potion = Item("Hyper Potion", "Healing", lambda target: target.heal(200), "Heals 200 HP")

max_potion = Item("Max Potion", "Healing", lambda target: target.full_heal(), "Heals to full HP")
