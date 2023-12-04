with open("games.txt", "r") as file:
    games_list = file.read().split("\n")

games = 0
green = 0
blue = 0
red = 0

available_red = 12
available_green = 13
available_blue = 14

game_possible = None, None

for game in games_list:
    step_one = game.split(":")
    current_game = step_one[0].split()[1]
    game_possible = True, current_game
    current_game_sets = step_one[1].split(";")
    for set_ in current_game_sets:
        subset = set_.split(',')
        for set_draw in subset:
            set_draw_item = set_draw.strip().split()
            match set_draw_item[1]:
                case "red":
                    red += int(set_draw_item[0])
                    if red > available_red:
                        game_possible = False, current_game
                case "green":
                    green += int(set_draw_item[0])
                    if green > available_green:
                        game_possible = False, current_game
                case "blue":
                    blue += int(set_draw_item[0])
                    if blue > available_blue:
                        game_possible = False, current_game
                    
        green, blue, red = 0, 0, 0

    if game_possible[0]:
        print(f"This game, {current_game} is possible.")
        games += int(game_possible[1])

print(games)
    
