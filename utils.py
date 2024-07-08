import time
import sys
from tabulate import tabulate

def slow_print(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def show_pokemon_table(pokemon_list, show_current_health):
    table = []
    for pokemon in pokemon_list:
        move_names = ', '.join(move.name for move in pokemon.moves) if pokemon.moves else "None"
        table.append([
            pokemon.name,
            pokemon.type,
            str(pokemon.current_health) + " out of max health " + str(pokemon.max_health) if show_current_health else str(pokemon.max_health) + " (Max)",
            move_names,
        ])

    headers = ["Name", "Type", "Health", "Moves"]

    slow_print(tabulate(table, headers, tablefmt="grid"), 0.01)
