from classes import Person, fights

if __name__ == "__main__":
    player1 = Person(name="Jhon", health=400, attack=95, defense=60, critical_chance=0.1)  
    player2 = Person(name="Brendon", health=278, attack=65, defense=4, critical_chance=0.5)  
    fights(player1, player2)