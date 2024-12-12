import random
import time 

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 15
        self.inventory = []
    
    def attack_enemy(self, enemy):
        damage = random.randint(self.attack - 5, self.attack + 5)
        enemy.hp -= damage
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        return damage

    def heal(self):
        if "Health Potion" in self.inventory:
            self.hp += 30
            self.hp = min(self.hp, 100)
            self.inventory.remove("Health Potion")
            print(f"{self.name} used a Health Potion and restored 30 HP!")
        else:
            print(f"{self.name} has no Health Potions left!")


class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_player(self, player):
        damage = random.randint(self.attack - 5, self.attack + 5)
        player.hp -= damage
        print(f"{self.name} attacks {player.name} for {damage} damage!")
        return damage


def display_stats(player, enemy):
    print(f"\n{player.name}'s HP: {player.hp}")
    print(f"{enemy.name}'s HP: {enemy.hp}\n")


def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")
    while player.hp > 0 and enemy.hp > 0:
        display_stats(player, enemy)
        action = input("Choose an action: (1) Attack (2) Heal: ")
        if action == "1":
            player.attack_enemy(enemy)
            if enemy.hp > 0:
                enemy.attack_player(player)
        elif action == "2":
            player.heal()
            if enemy.hp > 0:
                enemy.attack_player(player)
        else:
            print("Invalid choice!")

        if player.hp <= 0:
            print(f"\n{player.name} has been defeated by {enemy.name}...")
            return False
        elif enemy.hp <= 0:
            print(f"\n{player.name} has defeated {enemy.name}!")
            player.inventory.append("Health Potion")
            print(f"{player.name} found a Health Potion!")
            return True


def main():
    print("Welcome to Dungeon Quest!")
    name = input("Enter your character's name: ")
    player = Player(name)
    print(f"Welcome, {player.name}! Your adventure begins...\n")

    enemies = [
        Enemy("Goblin", 30, 10),
        Enemy("Skeleton", 40, 12),
        Enemy("Orc", 50, 15),
        Enemy("Dark Wizard", 60, 18),
        Enemy("Dragon", 100, 25)
    ]

    for enemy in enemies:
        if not battle(player, enemy):
            print("Game Over!")
            return

        print(f"{player.name} takes a short rest to recover...\n")
        time.sleep(2)

    print(f"Congratulations, {player.name}! You have conquered the dungeon and emerged victorious!")


if __name__ == "__main__":
    main()
