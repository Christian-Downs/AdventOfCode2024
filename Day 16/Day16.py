start_symbol = "S"
start_spot = []
facing = "E"
end_symbol = "E"
end_spot = []
score = 0
wall = "#"
position = []
map_file = "map.txt"
map = []
player = "p"
last_location = []
normal_symbol = "."
places_ive_been = []


def main():
    get_map()
    update_map()
    while position[0] != end_spot[0] and position[1] != end_spot[1]:
        if not move_forward():
            turn_right()
        update_map()


def get_map():
    global map
    f = open(map_file, "r")
    y = 0
    for line in f:
        map.append([])
        x = 0
        for space in line:
            map[y].append(space)
            x += 1
            if space == start_symbol:
                global start_spot
                start_spot = [x, y]
                global position
                position = start_spot
            if space == end_symbol:
                global end_spot
                end_spot = [x, y]
        y += 1
    f.close()


def move_forward():
    global position
    global score
    global last_location
    moved = False
    match facing:
        case "E":
            if check_if_go_able(position[0] + 1, position[1]):
                moved = True
                last_location = position.copy()
                position[0] += 1
        case "W":
            if check_if_go_able(position[0] - 1, position[1]):
                moved = True
                last_location = position.copy()
                position[0] -= 1
        case "N":
            if check_if_go_able(position[0], position[1] - 1):
                moved = True
                last_location = position.copy()
                position[1] -= 1
        case "S":
            if check_if_go_able(position[0], position[1] + 1):
                moved = True
                last_location = position.copy()
                position[1] += 1
    if moved:
        score += 1
    return moved


def check_if_go_able(x, y) -> bool:
    if map[y][x] != wall:
        return True
    else:
        return False


def update_map():
    global map

    map[position[1]][position[0]] = player
    if last_location != []:
        map[last_location[1]][last_location[0]] = normal_symbol
    print_map()


def turn_right():
    global facing
    match facing:
        case "E":
            facing = "S"
        case "W":
            facing = "N"
        case "N":
            facing = "E"
        case "S":
            facing = "W"


def turn_left():
    global facing
    match facing:
        case "E":
            facing = "N"
        case "W":
            facing = "S"
        case "N":
            facing = "W"
        case "S":
            facing = "E"


def print_map():
    output = ""
    output += "facing: " + facing + "\n"
    output += "position: " + str(position) + "\n"
    for line in map:
        output += (''.join(line))
    print(output)


main()
