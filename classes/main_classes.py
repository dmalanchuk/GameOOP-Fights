import random

class Person:
    def __init__(self, name, health, attack, defense, critical_chance):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.critical_chance = critical_chance
        
    def attack_enemy(self, enemy):
        is_critical = self.critical_hit()
        damage = max(self.attack - self.defense, 0)
        if is_critical:
            damage *= 2
            print(f'Critical hit by {self.name}')
        enemy.health = max(enemy.health - damage, 0)
        print(f"{self.name} attacks {enemy.name} for {damage} damage. {enemy.name}'s health: {enemy.health}")
        
    def critical_hit(self):
        return random.random() < self.critical_chance        
    
    
def fights(player1, player2):
    round_number = 1
    while player1.health > 0 and player2.health > 0:
        print(f"\n--- Round {round_number} ---")
        player1.attack_enemy(player2)
        if player2.health == 0:
            print(f"\n{player1.name} wins! Remaining health: {player1.health}")
            break
        player2.attack_enemy(player1)
        if player1.health == 0:
            print(f"\n{player2.name} wins! Remaining health: {player2.health}")
            break
        round_number += 1

if __name__ == "__main__":
    player1 = Person(name="Jhon", health=400, attack=95, defense=60, critical_chance=0.1)  
    player2 = Person(name="Brendon", health=278, attack=65, defense=4, critical_chance=0.5)  
    fights(player1, player2)