from class_defn.pokemon import Pokemon
from random import choice
from utils import slow_print, show_pokemon_table

class Trainer:
    def __init__(self, name, team, inventory):
        self.name = name
        self.team = team
        self.inventory = inventory

    def catch_pokemon(self, wild_pokemon):
        if wild_pokemon.is_wild and len(self.team) < 6:
            self.team.append(wild_pokemon)
            wild_pokemon.is_wild = False
            slow_print(f"\n{self.name} caught {wild_pokemon.name}!")
        else:
            slow_print("\nCan't catch this Pokémon!")

    def receive_item(self, item):
        self.inventory.append(item)
        slow_print(f"\n{self.name} received {item.name}!")
        slow_print(f"This item has the corresponding effect: {item.description}")

    def use_item(self, item, target):
        item.use(target)

    def show_inventory(self):
        slow_print(f"\n{self.name}'s Inventory:")
        for idx, item in enumerate(self.inventory):
            slow_print(f"{idx + 1}. {item.name} ({item.description})")

    def show_team(self):
        show_pokemon_table(self.team, True)

    def battle(self, opponent):
        slow_print(f"\n{self.name} is battling {opponent.name}!")
        my_pokemon = self.team[0]
        opponent_pokemon = opponent.team[0]

        while my_pokemon.current_health > 0 and opponent_pokemon.current_health > 0:
            slow_print(f"\n{my_pokemon.name} (HP: {my_pokemon.current_health}) vs {opponent_pokemon.name} (HP: {opponent_pokemon.current_health})")

            move = self.choose_move(my_pokemon)
            my_pokemon.attack_opponent(move, opponent_pokemon)

            if opponent_pokemon.current_health > 0:
                move = choice(opponent_pokemon.moves)
                opponent_pokemon.attack_opponent(move, my_pokemon)

        if my_pokemon.current_health > 0:
            slow_print(f"\n{my_pokemon.name} won the battle!")
            self.gain_experience(100)
            return True
        else:
            slow_print(f"\n{my_pokemon.name} fainted!")
            return False

    def choose_move(self, pokemon):
        slow_print(f"\nChoose a move for {pokemon.name}:", 0.02)
        for idx, move in enumerate(pokemon.moves):
            slow_print(f"{idx + 1}. {move.name} ({move.type} type, {move.power} power, {move.accuracy}% accuracy)", 0.02)
        while (True):
            try:
                choice = int(input("\nEnter the number of the move you want to use: ")) - 1
                break
            except:
                slow_print("\nInvalid. Try again.")
        return pokemon.moves[choice]

    def gain_experience(self, exp):
        for pokemon in self.team:
            pokemon.gain_experience(exp)
