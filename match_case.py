player_class = "Warrior"

#maak 6 waarden classem en 1 onbekende class
match player_class:
    case "Warrior":
        print("Je hebt een warrior gekozen!")
        player_health = 150
        player_damage = 20
        print("Player health:", player_health)
        print("Player damage:", player_damage)
    case "Mage":
        print("Je hebt een mage gekozen!")
        player_health = 80
        player_damage = 35
        print("Player health:", player_health)
        print("Player damage:", player_damage)
    case "Archer":
        print("Je hebt een archer gekozen!")
        player_health = 100
        player_damage = 25
        print("Player health:", player_health)
        print("Player damage:", player_damage)
    case "Rogue":
        print("Je hebt een rogue gekozen!")
        player_health = 90
        player_damage = 30
        print("Player health:", player_health)
        print("Player damage:", player_damage)
    case "Assassin":
        print("Je hebt een assassin gekozen!")
        player_health = 85
        player_damage = 40
        print("Player health:", player_health)
        print("Player damage:", player_damage)
    case "Goblin":
        print("Je hebt een goblin gekozen!")
        player_health = 90
        player_damage = 25
        print("Player health:", player_health)
        print("Player damage:", player_damage)
    case _:
        print("Onbekende class") 