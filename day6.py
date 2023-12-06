from math import ceil, floor

times = [47, 98, 66, 98]
distances = [400, 1213, 1011, 1540]

times2 = [47986698]
distances2 = [400121310111540]

def calc_num_ways (arg_times, arg_distances):
    num_ways_to_beat_record = 1
    for idx, t in enumerate(arg_times):
        # res = x^2 - t*x + distances[idx] = 0
        # a = 1, b = -t, c = distances[idx]
        # => quadratic formula
        
        root1 = 0.5 * (t + (t**2 - 4 * arg_distances[idx])**0.5)
        if int(root1) == root1:
            root1 -= 1

        root2 = 0.5 * (t - (t**2 - 4 * arg_distances[idx])**0.5)
        if int(root2) == root2:
            root2 += 1

        num_ways_to_beat_record *= (floor(root1) - ceil(root2) + 1)
    return num_ways_to_beat_record

# part 1
print(calc_num_ways(times, distances))

# part 2
print(calc_num_ways(times2, distances2))