class Person:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        
    def attack_enemy(self, enemy):
        damage = max(self.attack - enemy.defense, 0)
        enemy.health = max(enemy.health - damage, 0)
        

def fights(player1, player2):
    while player1.health > 0 and player2.health > 0:
        player1.attack_enemy(player2)
        player2.attack_enemy(player1)
    if player1.health == 0:
        print(f"{player2.name} wins! Remaining health: {player2.health}")
    else:
        print(f"{player1.name} wins! Remaining health: {player1.health}")

if __name__ == "__main__":
    john = Person("John", 100, 20, 10)
    alice = Person("Alice", 100, 35, 5)
    fights(john, alice)