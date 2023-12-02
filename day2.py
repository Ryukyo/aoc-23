import regex as re

sum_possible = 0
bag_limit = {
    "red": 12, 
    "green": 13, 
    "blue": 14
}

with open('day2.txt', 'r') as f:
    for idx, line in enumerate(f.readlines()):
        valid = True
        line.strip()
        game, results = line.split(": ")
        game_id = game.split(" ")[1]
        round_data = re.findall(r"\d+\s(?:red|blue|green)", results)

        for element in round_data:
            data = element.split(" ")
            value = int(data[0])
            color = data[1]
            
            if value > bag_limit[color]:
                valid = False

        if valid:
            sum_possible += int(game_id)
    print(sum_possible)