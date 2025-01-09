class Person:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        
    def attack_enemy(self, enemy):
        damage = max(self.attack - enemy.defense, 0)
        enemy.health = max(enemy.health - damage, 0)
        


if __name__ == "__main__":
    pass