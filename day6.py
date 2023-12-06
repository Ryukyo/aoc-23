from math import prod, ceil, floor

times = [47, 98, 66, 98]
distances = [400, 1213, 1011, 1540]

num_ways_to_beat_record = 1

for idx, t in enumerate(times):
    # res = x^2 - t*x + distances[idx] = 0
    # a = 1, b = -t, c = distances[idx]
    # => quadratic formula
    
    root1 = 0.5 * (t + (t**2 - 4*distances[idx])**0.5)
    if int(root1) == root1:
        root1 -= 1

    root2 = 0.5 * (t - (t**2 - 4*distances[idx])**0.5)
    if int(root2) == root2:
        root2 += 1

    num_ways_to_beat_record *= (floor(root1) - ceil(root2) + 1)

# part 1
print(num_ways_to_beat_record)