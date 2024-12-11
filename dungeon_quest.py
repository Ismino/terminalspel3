import random
import time 

class Player:
    def __init__(self, name):
        self.name = nameself.hp = 100
        self.attack = 15
        self.inventory = []
    
    def attack_enemy(self, enemy):
        damage = random.randint(self.attack - 5, self.attack + 5)
        enemy.hp -= damage
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        return damage

    def heal(self):
        if "Healt Potion" in self.inventory:
            self.hp += 30
            self.hp = min(self.hp, 100)
            self.inventory.remove("Healt Potion")
            print(f"{self.name} used a Healt Potion and restored 30 hp")
        else:
            print(f"{self.name} has no Healt Potions left!")

class Enemy:
    def __init__(self,name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_player(self, player):
        damage = random.randint(self.attack -5, self.attack + 5)
        player.hp -= damage
        print(f"{self.name} attacks {player.name} for {damage} damage")
        return damage

    def display_stats(player, enemy):
        print(f"\n{player.name}'s HP: {player.hp}")
        print(f"{enem.name}'s HP: {enemy.hp}\n")

    def battle(player, enemy):
        print(f"A wild {enemy.name} appears!")
        while player.hp > 0 and enemy.hp > 0:
            display_stats(player, enemy)
            