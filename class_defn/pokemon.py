import random
from class_defn.move import Move
from utils import slow_print

class Pokemon:
    def __init__(self, name, type, health, attack, defense, special_attack, special_defense, speed, level, experience, moves, is_wild):
        self.name = name
        self.type = type
        self.max_health = health
        self.current_health = health
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        self.level = level
        self.experience = experience
        self.moves = moves
        self.is_wild = is_wild

    def attack_opponent(self, move, opponent):
        slow_print(f"\n{self.name} used {move.name}!")
        if random.random() <= move.accuracy:
            damage = self.calculate_damage(move, opponent)
            opponent.take_damage(damage)
            move.apply_effect(opponent)
        else:
            slow_print(f"\n{self.name}'s attack missed!")

    def calculate_damage(self, move, opponent):
        if move.category == "Physical":
            damage = ((2 * self.level / 5 + 2) * move.power * self.attack / opponent.defense) / 50 + 2
        else:
            damage = ((2 * self.level / 5 + 2) * move.power * self.special_attack / opponent.special_defense) / 50 + 2

        return int(damage)

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0
        slow_print(f"\n{self.name} took {damage} damage! Current health: {self.current_health}")

    def gain_experience(self, exp):
        self.experience += exp
        if self.experience >= self.level ** 3:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_health += 10
        self.attack += 2
        self.defense += 2
        self.special_attack += 2
        self.special_defense += 2
        self.speed += 2
        self.current_health = self.max_health
        slow_print(f"\n{self.name} leveled up to level {self.level}!")

    def learn_move(self, move):
        if len(self.moves) < 4:
            self.moves.append(move)
        else:
            slow_print(f"\n{self.name} can't learn more than 4 moves!")

    def get_stat(self, stat):
        return getattr(self, stat)

    def full_heal(self):
        self.current_health = self.max_health
        slow_print(f"\n{self.name} has been fully healed!")

    def heal(self, amount = 0):
        if (self.current_health + amount >= self.max_health):
            self.full_heal()
        else:
            self.current_health += amount
            slow_print(f"\n{self.name} has been healed!")
            slow_print(f"{self.name} has {self.current_health} health!")
