from class_defn.move import Move
from class_defn.pokemon import Pokemon

ember = Move(name="Ember", type="Fire", power=40, accuracy=100, category="Special")
scratch = Move(name="Scratch", type="Physical", power=40, accuracy=100, category="Physical")
growl = Move(name="Growl", type="Physical", power=0, accuracy=100, category="Status", effect=lambda target: print(f"{target.name}'s Attack fell!"))

charmander = Pokemon(
    name="Charmander",
    type="Fire",
    health=39,
    attack=52,
    defense=43,
    special_attack=60,
    special_defense=50,
    speed=65,
    level=5,
    experience=0,
    moves=[ember, scratch, growl],
    is_wild=False
)
