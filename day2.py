import regex as re
import math

sum_possible = 0
bag_limit = {
    "red": 12, 
    "green": 13, 
    "blue": 14
}

round_max = {}
i = 1

with open('day2.txt', 'r') as f:
    for idx, line in enumerate(f.readlines()):
        valid = True
        round_max[i] = {}

        game, results = line.split(": ")
        game_id = game.split(" ")[1]
        round_data = re.findall(r"\d+\s(?:red|blue|green)", results)

        for element in round_data:
            data = element.split(" ")
            value = int(data[0])
            color = data[1]
            
            if value > bag_limit[color]:
                valid = False

            # get the maximum of each 
            if color not in round_max[i]:
                round_max[i][color] = value
            if value > round_max[i][color]:
                round_max[i][color] = value
        
        i += 1
        if valid:
            sum_possible += int(game_id)

    print(sum_possible)

    t_num = 0

    for nums in round_max.values():
        t_num += math.prod(nums.values())

    print(t_num)