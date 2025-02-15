import random

def main():
    # Ask the player for their name and initialize player stats
    player_name = input("Enter your name, brave adventurer: ")
    player = {
        'name': player_name, 
        'health': 20, 
        'attack': 6, 
        'defense': 4, 
        'level': 1, 
        'magic': 0,
        'enemies_defeated': 0
    }
    
    levels = {
        1: ['Entrance', 'Dark Hallway one', 'Abandoned Library'],
        2: ['Entrance', 'Dark Hallway one', 'Abandoned Library', 'Dark Hallway two', 'Monster Lair'],
        3: ['Entrance', 'Dark Hallway one', 'Abandoned Library', 'Dark Hallway two', 'Monster Lair', 'Dark Hallway three', 'Hidden Crypt'],
        4: ['Entrance', 'Dark Hallway one', 'Abandoned Library', 'Dark Hallway two', 'Monster Lair', 'Dark Hallway three', 'Hidden Crypt', 'Dark Hallway four', 'Armory'],
        5: ['Final Boss Chamber']
    }
    
    enemy_requirements = {1: 2, 2: 4, 3: 6, 4: 8, 5: 1}

    print(f"Welcome to the Mini Dungeon Crawl, {player_name}!")
    
    while player['health'] > 0 and player['level'] <= 5:
        print(f"\n--- Level {player['level']} ---")
        print_player_stats(player)
        
        if player['enemies_defeated'] >= enemy_requirements[player['level']]:
            if player['level'] == 5:
                print("\nYou have reached the Final Boss Chamber!")
                if combat(player, "The Final Dungeon Boss", 25, 7, 7):
                    print("\nCongratulations! You have conquered the dungeon!")
                else:
                    print("\nYou were slain by the Final Dungeon Boss. Game Over.")
                return
            else:
                level_up(player)
        
        print("\nRooms available:")
        for i, room in enumerate(levels[player['level']], 1):
            print(f"{i}. {room}")

        choice = input("Which room would you like to enter? (Enter a number): ")
        if choice.isdigit() and 1 <= int(choice) <= len(levels[player['level']]):
            explore_room(levels[player['level']][int(choice) - 1], player)
        else:
            print("Invalid choice. Try again.")

        if player['health'] <= 0:
            print(f"\n{player_name}, you have perished in the dungeon! Game Over.")
            return

def print_player_stats(player):
    print(f"\n{player['name']} - Level {player['level']} Stats:")
    print(f"Health: {player['health']} | Attack: {player['attack']} | Defense: {player['defense']} | Magic: {player['magic']}")
    print(f"Enemies defeated: {player['enemies_defeated']}")

def level_up(player):
    player['level'] += 1
    player['health'] += 8
    player['attack'] += 4
    player['magic'] += 2
    print("\nCongratulations! You leveled up!")
    print_player_stats(player)

def explore_room(room, player):
    print(f"\nYou enter the {room}.")

    # for Final Boss Chamber at Level 5
    if player['level'] == 5 and room == "Final Boss Chamber":
        print("\nYou have reached the Final Boss Chamber!")
        combat(player, "The Final Dungeon Boss", 25, 7, 7)
        return

    if random.choice([True, False]):
        encounter_enemy(player)
    else:
        print("The room is eerily quiet, but you find something useful.")
        find_item(player)

def encounter_enemy(player):
    enemies = {
        "Warrior": (5, 3, 1),
        "Greedy Goblin": (6, 3, 1),
        "Sneaky Rogue": (10, 4, 2),
        "Cunning Scout": (11, 4, 2),
        "Evil Wizard": (13, 5, 3),
        "Street Brawler": (12, 5, 3),
        "Wise Spirit": (9, 6, 2),
        "Dungeon Guardian": (15, 5, 3),
    }

    level_enemies = {
        1: ["Warrior", "Greedy Goblin"],
        2: ["Warrior", "Greedy Goblin", "Sneaky Rogue", "Cunning Scout"],
        3: ["Warrior", "Greedy Goblin", "Sneaky Rogue", "Cunning Scout", "Evil Wizard", "Street Brawler"],
        4: ["Warrior", "Greedy Goblin", "Sneaky Rogue", "Cunning Scout", "Evil Wizard", "Street Brawler", "Dungeon Guardian"],
    }

    # Prevent normal enemies from spawning at level 5
    if player['level'] == 5:
        return  

    enemy_name = random.choice(level_enemies[player['level']])
    enemy_health, enemy_attack, enemy_defense = enemies[enemy_name]
    
    print(f"\nA {enemy_name} appears!")

    action = input("Do you want to fight or flee? (fight/flee): ").strip().lower()
    if action == "fight":
        if combat(player, enemy_name, enemy_health, enemy_attack, enemy_defense):
            player['enemies_defeated'] += 2
    else:
        print("You flee, but the enemy strikes you while escaping!")
        player['health'] -= random.randint(5, 15)

def combat(player, enemy_name, enemy_health, enemy_attack, enemy_defense):
    print(f"\nBattle starts against {enemy_name}!")

    while player['health'] > 0 and enemy_health > 0:
        player_damage = max(1, random.randint(1, player['attack']) - enemy_defense)
        enemy_damage = max(1, random.randint(1, enemy_attack) - player['defense'])

        print(f"\nYou attack and deal {player_damage} damage!")
        enemy_health -= player_damage

        if enemy_health <= 0:
            print(f"You defeated the {enemy_name}!")
            return True

        print(f"The {enemy_name} attacks and deals {enemy_damage} damage!")
        player['health'] -= enemy_damage

    if player['health'] <= 0:
        print(f"You were slain by the {enemy_name}.")
        return False

def find_item(player):
    items = ['Health Potion', 'Attack Boost', 'Defense Shield', 'Magic Rune']
    found = random.choice(items)
    print(f"You found a {found}!")

    if found == 'Health Potion':
        player['health'] += 5
        print("You feel rejuvenated!")
    elif found == 'Attack Boost':
        player['attack'] += 2
        print("Your attack power has increased!")
    elif found == 'Defense Shield':
        player['defense'] += 1
        print("Your defense has improved!")
    elif found == 'Magic Rune':
        player['magic'] += 1
        print("Your magical power grows stronger!")

if __name__ == "__main__":
    main()
