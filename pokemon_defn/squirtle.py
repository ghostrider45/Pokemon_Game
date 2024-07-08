from class_defn.move import Move
from class_defn.pokemon import Pokemon

water_gun = Move(name="Water Gun", type="Water", power=40, accuracy=100, category="Special")
tackle = Move(name="Tackle", type="Physical", power=40, accuracy=100, category="Physical")
tail_whip = Move(name="Tail Whip", type="Physical", power=0, accuracy=100, category="Status", effect=lambda target: print(f"{target.name}'s Defense fell!"))

squirtle = Pokemon(
    name="Squirtle",
    type="Water",
    health=44,
    attack=48,
    defense=65,
    special_attack=50,
    special_defense=64,
    speed=43,
    level=5,
    experience=0,
    moves=[water_gun, tackle, tail_whip],
    is_wild=False
)
