"""
Your name: David Lee
Your student number: A01251357

All of your code must go in this file.
"""
import random


def title_screen():
    print("|------------|")
    print("| WELCOME TO |")
    print("|  A WORLD   |")
    print("| OF FANTASY,|")
    print("| _ _ _ _ _ _|")


def game():
    """
    Control the flow of the game

    """
    title_screen()
    rows = 25
    columns = 25
    board = make_board(rows, columns)
    character = make_character()
    achieved_goal = False
    while is_alive(character) and not achieved_goal:
        make_map(character)
        print(describe_current_location(board, character))
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            if character["X-coordinate"] == 13 and character["Y-coordinate"] == 14 and character["Level"] == 3:
                monster = make_boss()
                print("You have stumbled upon Rimuru! The final challenge!")
                battle_system(character, monster)
                achieved_goal = check_if_goal_attained(monster)
            else:
                there_is_a_challenger = check_for_foes()
                if there_is_a_challenger:
                    monster = make_monster()
                    print(f"A {monster['Name']} has appeared!")
                    battle_system(character, monster)
        else:
            print("You cannot move in that direction")
        if not is_alive(character):
            return print("You have died.")
    print("Congratulations you have beat the game.")


def make_character():
    """Stores the X and Y coordinates and the current HP of the character

    :precondition: a dictionary that include the coordinates and Health, Experience, Level and Attack.
    :postcondition: return character
    :return: a dictionary (character) that holds X,Y coordinates, Health, Experience, Level and Attack.


    """
    character = {"X-coordinate": 0, "Y-coordinate": 0, "Health": 100, "Experience": 0, "Level": 1, "Attack": 10}
    name = input("Welcome Adventurer, what is your name?: ")
    character["Name"] = name
    choose_your_class(character)
    return character


def choose_your_class(character):
    """Pick your class

    :param character: a dictionary containing character data.
    :precondition: must be a dictionary containing data
    :postcondition: user must input a correct input 1-4
    :return: user input that corresponds to class.
    """
    classes = {"1": "Shadow",
               "2": "Monk",
               "3": "Paladin",
               "4": "Mage"}
    continue_looping = True
    while continue_looping:
        class_selection = input("These are the three class choices available to you. \n"
                                "The first option is [1]Rogue.\n"
                                "It is a class that is capable of sneaky combat and nimble tricks.\n"
                                "A Shadow is stealthy and dexterous.\n"
                                "Are you ready to welcome the shadows?\n"
                                "If Shadow seems like a befitting choice enter 1.\n\n"
                                "The next choice would be [2] The Monk. Monks are the masters of martial arts.\n"
                                "A Monk is are calm and centered. If Monk seems like your choice, enter [2].\n\n"
                                "The last choice is a the Paladin class.\n"
                                "A Paladin is a holy knight, a champion for the name of good and order.\n"
                                "If you wish to join the holy order, enter [3].\n\n"
                                "Your last option will be [4] Mage. A mage is a master of the arcane.\n")
        if class_selection in classes:
            return make_classes(character, classes[class_selection])
        print("You have entered an invalid choice. Select again.")


def make_classes(character, classes):
    """Make a character class.

    :param character: a dictionary.
    :param classes: a dictionary.
    :precondition: character dictionary must contain character data.
    :precondition: class dictionary containing class data.
    :postcondition: combines class data into character data
    :return: character dictionary with class data.

    >>> make_classes(character={"Health": 100, "Experience": 0, "Level": 1, "Attack": 10}, classes = "Shadow")
    {'Health': 115, 'Experience': 0, 'Level': 1, 'Attack': 25, 'Class': 'Shadow', 'Special Attack': 'Back Stab'}

    >>> make_classes({"Health": 100, "Experience": 0, "Level": 1, "Attack": 10}, classes = "Mage")
    {'Health': 100, 'Experience': 0, 'Level': 1, 'Attack': 45, 'Class': 'Mage', 'Special Attack': 'Fireball'}
    """
    if classes == "Shadow":
        character["Health"] += 15
        character["Attack"] += 15
        character["Class"] = "Shadow"
        character["Special Attack"] = "Back Stab"
    elif classes == "Monk":
        character["Health"] += 25
        character["Attack"] += 10
        character["Class"] = "Monk"
        character["Special Attack"] = "One Punch"
    elif classes == "Mage":
        character["Attack"] += 35
        character["Class"] = "Mage"
        character["Special Attack"] = "Fireball"
    else:
        character["Health"] += 50
        character["Attack"] += 5
        character["Class"] = "Paladin"
        character["Special Attack"] = "Crusader Strike"
    return character


def make_monster():
    """Make Monster.

    :postcondition: "randomly" generates a monster
    :return: generates a monster from the list of dictionaries.
    """
    monster_list = [{"Name": "goblin", "health": 20, "attack": 5, "experience": 10},
                    {"Name": "giant", "health": 40, "attack": 10, "experience": 10},
                    {"Name": "rat", "health": 20, "attack": 5, "experience": 10},
                    {"Name": "wolf", "health": 20, "attack": 5, "experience": 10},
                    {"Name": "slime", "health": 20, "attack": 5, "experience": 10},
                    {"Name": "bandit", "health": 35, "attack": 15, "experience": 10},
                    ]

    return monster_list[random.randint(0, 5)]


def make_board(rows, columns):
    """
    Populate the board with a number of rows and columns.

    :param rows: an integer.
    :param columns: an integer.
    :precondition: number must be a positive integer equal to or greater than zero
    :precondition: number must be a positive integer equal to or greater than zero
    :postcondition: row will iterate through a for loop to create rows.
    :postcondition: column will iterate through a for loop to create columns.
    :return: returns the board with coordinate values stored as a tuple with rooms.
    """

    board = {}
    land_descriptions = ['You are in a Grass Field',
                         'You are in a Plains',
                         'You are in a Swamp',
                         'You are in a Forest',
                         'You are in a Mountains',
                         'You are in a Peninsula',
                         'You are in a Beach',
                         'You are in a Misty RainForest']
    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = random.choice(land_descriptions)
    board[(13, 14)] = "Boss Room"
    return board


def make_map(character):
    """Creates map

    :param character: a dictionary containing character data.
    :precondition: dictionary must contain data.
    :postcondition: creates map
    :return: displays a map with a symbol representing the character.
    """
    y_coordinate = character["Y-coordinate"]
    x_coordinate = character["X-coordinate"]
    board = make_board(25, 25)
    for column in range(y_coordinate - 2, y_coordinate + 3):
        for row in range(x_coordinate - 2, x_coordinate + 3):
            if column == y_coordinate and row == x_coordinate:
                print("[@]", end=" ")
            elif row == 13 and column == 14:
                print("!!!", end=" ")
            elif (row, column) in board:
                print("[#]", end=" ")
        print()
    return print(character)


def describe_current_location(board, character):
    """
    Describe the current location of the character in relation to the board.

    :param board: a dictionary containing map descriptions.
    :param character: a dictionary containing character information.
    :precondition: there must be a row and column value in board.
    :precondition: the X and Y coordinates must be in a range between 0 to 3.
    :postcondition: checks if the X and Y coordinate of character is within board
    :postcondition: gathers the X and Y coordinate of character dictionary
    :return: the current location of character on the board.
    """
    x_coordinate = character["X-coordinate"]
    y_coordinate = character["Y-coordinate"]
    current_location = x_coordinate, y_coordinate
    return board[current_location]


def get_user_choice():
    """
    Ask for user input to determine which direction to move character.

    :precondition: input for user must be a number between 1 to 4.
    :postcondition: determine if the user has inputted a valid choice.
    :return: the direction choice of user.
    """
    direction_choice = {"1": "NORTH", "2": "SOUTH", "3": "WEST", "4": "EAST"}
    continue_looping = True
    while continue_looping:
        user_input = input("Which direction would you like to go? \n[1]NORTH, [2]SOUTH, [3]WEST, or [4]EAST? : ")
        if user_input not in direction_choice:
            print("You have selected an invalid direction, select again.")
            continue
        return direction_choice[user_input]


def move_character(character, direction):
    """
    Move character in specific direction.

    :param character: a dictionary containing character data.
    :param direction: a dictionary containing direction
    :precondition: must contain character data
    :precondition: must have selected a valid direction
    :postcondition: will calculate new character coordinates depending on direction
    :postcondition: depending on direction selected, will add or subtract 1 from current coordinates.
    :return: character with new coordinate values.

    >>> move_character(character={"X-coordinate":0}, direction ="EAST")
    {'X-coordinate': 1}
    >>> move_character(character={"Y-coordinate":0}, direction="SOUTH")
    {'Y-coordinate': 1}

    """
    if direction == "EAST":
        character["X-coordinate"] += 1
    elif direction == "WEST":
        character["X-coordinate"] -= 1
    elif direction == "SOUTH":
        character["Y-coordinate"] += 1
    else:
        character["Y-coordinate"] -= 1
    return character


def validate_move(board, character, direction):
    """Validate the user choice of movement

    :param board: a dictionary containing map descriptions.
    :param character: a dictionary containing character information.
    :param direction: a dictionary containing character movement information.
    :precondition: there must be a row and column value in board.
    :precondition: the X and Y coordinates must be in a range between 0 to 3.
    :precondition: must be a valid directional choice: Up, Down, Right, Left.
    :postcondition: extract X and Y coordinate from board.
    :postcondition: extract X and Y locations from character dictionary
    :postcondition: a restraint on the new X and Y values.
    :return: True if the character movement is possible, if not, False.

    >>> validate_move(board=[(2,2)], character={"X-coordinate":0, "Y-coordinate":0}, direction="SOUTH")
    True
    >>> validate_move(board=[(2,2)], character={"X-coordinate":0, "Y-coordinate":0}, direction="NORTH")
    False
    """
    x_position = (character.get("X-coordinate"))
    y_position = (character.get("Y-coordinate"))
    directions = {"NORTH": -1, "SOUTH": 1, "WEST": -1, "EAST": 1}
    number_board_rows = max(board)[0] + 1
    if direction in ["NORTH", "SOUTH"]:
        new_y_position = y_position + directions[direction]
        if -1 < new_y_position < number_board_rows:
            return True
    elif direction in ["WEST", "EAST"]:
        new_x_position = x_position + directions[direction]
        if -1 < new_x_position < number_board_rows:
            return True
    return False


def check_for_foes():
    """Encounter a foe 20% of the time you move.

    :postcondition: randomly generates a number between 1 to 5.
    :return: Generate 1, True you encounter a foe. Numbers 2-5 False if you do not.
    """
    encounter_foe = random.randint(1, 5)
    if encounter_foe == 1:
        return True
    else:
        return False


def get_battle_choice():
    """Get battle user input

    :precondition: User must input a choice between 1 - 3.
    :return: depending on user input. It will return "ATTACK", "SPECIAL ATTACK" or "FLEE".
    """
    battle_choice = {"1": "ATTACK", "2": "SPECIAL ATTACK", "3": "FLEE"}
    continue_looping = True
    while continue_looping:
        user_input = input("What would you like to do in this battle? \n"
                           "[1] ATTACK \n"
                           "[2] SPECIAL ATTACK \n"
                           "[3] FLEE\n")
        if user_input not in battle_choice:
            print("You have selected an invalid choice. Select again")
        else:
            return battle_choice[user_input]


def calculate_player_damage(character, monster):
    """Calculate player damage

    :param character: a dictionary.
    :param monster: a dictionary.
    :precondition: dictionary must contain character data.
    :precondition: dictionary must contain monster data.
    :postcondition: takes an int, character attack.
    :postcondition: calculates damage taken.
    :return: monster health after taking damage.
    """
    monster['health'] -= character['Attack']
    damage = (character['Attack'])
    print(f"{character['Name']} hit {monster['Name']}. You dealt {damage} damage to {monster['Name']}.")


def calculate_special_attack_damage(character, monster):
    """Calculate special attack damage

    :param character: a dictionary.
    :param monster: a dictionary.
    :precondition: dictionary must contain character data.
    :precondition: dictionary must contain monster data.
    :postcondition: calculates attack damage.
    :postcondition: calculates health.
    :return: damage done to monster with special attack.
    """
    monster['health'] -= (character['Attack'] * 1.5)
    damage = (character['Attack'] * 1.5)
    print(f"{character['Name']} used {character['Special Attack']} and hit {monster['Name']}. You dealt {damage}"
          f" damage to {monster['Name']}.")


def calculate_monster_damage(character, monster):
    """Calculate monster damage

    :param character: a dictionary.
    :param monster: a dictionary.
    :precondition: dictionary must contain character data.
    :precondition: dictionary must contain monster data.
    :postcondition: calculates character health.
    :postcondition: calculate monster damage.
    :return: damage done to player with monster attack.
    """
    character['Health'] -= monster['attack']
    damage = monster['attack']
    print(f"{monster['Name']} hit {character['Name']}. {monster['Name']} dealt {damage}"
          f" damage to {character['Name']}.")


def monster_flee(monster):
    """Monster fleeing

    :param monster: a dictionary.
    :precondition: a dictionary that contains monster information.
    :postcondition: determines if the monster successfully fled.
    :return: True if Monster has fled. False if monster did not.
    """
    monster_flee_chance = random.randint(1, 5)
    if monster_flee_chance == 1:
        print('Monster has runaway')
        return True
    elif monster['Name']== "Rimuru":
        return False
    else:
        return False


def battle_system(character, monster):
    while monster['health'] > 0 and is_alive(character):
        choice = get_battle_choice()
        if choice == "ATTACK":
            calculate_player_damage(character, monster)
            if monster['health'] > 0:
                calculate_monster_damage(character, monster)
                if monster_flee(monster):
                    break
        elif choice == "SPECIAL ATTACK":
            calculate_special_attack_damage(character, monster)
            if monster['health'] > 0:
                calculate_monster_damage(character, monster)
                if monster_flee(monster):
                    break
        elif choice == "FLEE":
            hit_attempting_run = random.randint(1, 5)
            if hit_attempting_run == 1:
                print(f"You have failed to runaway! As a result, the {monster['Name']} has landed a successful hit!")
                calculate_monster_damage(character, monster)
                break
            else:
                print("You have ran away")
                break
    if monster['health'] <= 0 and monster['Name'] == "Rimuru":
        print("You have defeated the Boss of this game! Congratulations you have beat the game.")
    elif monster['health'] <= 0:
        print(f"{monster['Name']} has died.")
        character["Experience"] += monster['experience']
        print(f"You have gained {monster['experience']} experience from {monster['Name']}")
        level_up(character)


def check_if_goal_attained(monster):
    """Check if the goal has been reached.

    :param monster: a dictionary that contains boss information.
    :precondition: monster must contain values within its dictionary.
    :postcondition: Checks if character is dead or if monster Rimuru and Rimuru's health is 0.
    :return: True if the checks are met, if they're not, False.

    >>> check_if_goal_attained(monster={"Name": "Rimuru", "health": 0})
    True
    >>> check_if_goal_attained(monster={"Name": "goblin", "health": 0})
    False

    """
    if is_alive is False or monster['Name'] == "Rimuru" and monster['health'] <= 0:
        return True
    else:
        return False


def level_up(character):
    """Level up character

    :param character: a dictionary.
    :precondition: a dictionary containing character data.
    :postcondition: calculates new level of character and class advancement
    :return: character dictionary with updated level, attack, and class.

    """
    if character["Level"] != 3 and character["Experience"] >= 100:
        character["Level"] += 1
        character["Health"] += 25
        character["Attack"] += 10
        character["Experience"] -= 100
        print("Congratulations you have reached level", character["Level"])

    if character["Class"] == "Shadow" and character["Level"] == 2:
        character.update({"Class": "Trickster"})
        print("You have advanced to a Trickster")

    elif character["Class"] == "Monk" and character["Level"] == 2:
        character.update({"Class": "Templar"})
        print("You have advanced to a Templar")

    elif character["Class"] == "Mage" and character["Level"] == 2:
        character.update({"Class": "Elementalist"})
        print("You have advanced to a Elementalist")

    elif character["Class"] == "Paladin" and character["Level"] == 2:
        character.update({"Class": "Crusader"})
        print("You have advanced to a Crusader")

    elif character["Class"] == "Trickster" and character["Level"] == 3:
        character.update({"Class": "Assassin"})
        print("You have advanced to a Assassin")

    elif character["Class"] == "Templar" and character["Level"] == 3:
        character.update({"Class": "Inquisitor"})
        print("You have advanced to a Inquisitor")

    elif character["Class"] == "Elementalist" and character["Level"] == 3:
        character.update({"Class": "Ascendant"})
        print("You have advanced to a Ascendant")

    elif character["Class"] == "Crusader" and character["Level"] == 3:
        character.update({"Class": "White Knight"})
        print("You have advanced to a White Knight")

    return character


def is_alive(character):
    """
    Check if character is alive.

    :param character: a dictionary containing character information
    :precondition: character dictionary must contain current HP
    :postcondition: check if the current HP is above 0.
    :return: returns True if character has more than 0 hp. If Character reaches 0, returns False.
    >>> is_alive(character={"Health": 100})
    True
    >>> is_alive(character={"Health": 0})
    False
    >>> is_alive(character={"Health": -5})
    False
    """
    if character["Health"] > 0:
        return True
    else:
        return False


def make_boss():
    """Creates boss Rimuru.
    :postcondition: initializes boss Rimuru
    :return: dictionary containing boss data.
    """
    return {"Name": "Rimuru", "health": 150, "attack": 30}


def main():
    game()


if __name__ == "__main__":
    main()
