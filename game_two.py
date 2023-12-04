with open("games.txt", "r") as file:
    games_list = file.read().split("\n")

reds = []
greens = []
blues = []
total = 0

for game in games_list:
    step_one = game.split(":")
    current_game = step_one[0].split()[1]
    current_game_sets = step_one[1].split(";")
    for set_ in current_game_sets:
        subset = set_.split(',')
        for set_draw in subset:
            set_draw_item = set_draw.strip().split()
            match set_draw_item[1]:
                case "red":
                    reds.append(int(set_draw_item[0]))
                case "green":
                    greens.append(int(set_draw_item[0]))
                case "blue":
                    blues.append(int(set_draw_item[0]))
                    
        green, blue, red = 0, 0, 0

    reds_max = sorted(reds)[-1]
    greens_max = sorted(greens)[-1]
    blues_max = sorted(blues)[-1]
    game_power = reds_max * greens_max * blues_max
    total += game_power
    reds = []
    greens = []
    blues = []
print(total)