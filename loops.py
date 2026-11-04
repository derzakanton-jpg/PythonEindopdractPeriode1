#onze variablen
monsters = [100, 150, 250]
player_damage = 25
attack_count = 0

#gebruik de goede code om het monster te vallen
for monster_health in monsters:
    while monster_health > 0:
        print("Nu monster heeft", monster_health, "health!")
        monster_health = monster_health - player_damage
        attack_count += 1
        if monster_health == 0:
            print("Monster is verslaagd!")
            print("Je hebt", attack_count, "attacks nodig voor monster te aanvallen")
            attack_count = 0