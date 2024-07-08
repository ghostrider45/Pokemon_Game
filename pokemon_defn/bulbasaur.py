from class_defn.move import Move
from class_defn.pokemon import Pokemon

vine_whip = Move(name="Vine Whip", type="Grass", power=45, accuracy=100, category="Physical")
leech_seed = Move(name="Leech Seed", type="Grass", power=0, accuracy=90, category="Status", effect=lambda target: print(f"{target.name} was seeded!"))
growl_bulbasaur = Move(name="Growl", type="Physical", power=0, accuracy=100, category="Status", effect=lambda target: print(f"{target.name}'s Attack fell!"))

bulbasaur = Pokemon(
    name="Bulbasaur",
    type="Grass/Poison",
    health=45,
    attack=49,
    defense=49,
    special_attack=65,
    special_defense=65,
    speed=45,
    level=5,
    experience=0,
    moves=[vine_whip, leech_seed, growl_bulbasaur],
    is_wild=False
)
