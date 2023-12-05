import re
from functools import reduce

almanac = open("day5.txt").read().rstrip()
entries = almanac.split("\n\n")
seeds = list(map(int, re.findall(r"\d+", entries[0])))

maps = []
for mp in entries[1:]:
    m = []
    for line in mp.split("\n")[1:]:
        end, start, delta = map(int, re.findall(r"\d+", line))
        m.append([start, start + delta - 1, end - start])
    maps.append(sorted(m))

def lookup(s, map):
    for start, end, delta in map:
        if   s > end: continue
        elif s < start: return s
        else: return s + delta
    return s

locations  = [reduce(lookup, maps, s) for s in seeds]

print(f"Part1: {min(locations)}")