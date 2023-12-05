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

def lookup(s, m):
    for start, end, delta in m:
        if   s > end: continue
        elif s < start: return s
        else: return s + delta
    return s

def lookup2(s, t, m):
    rs = []

    for start, end, delta in m:
        # start.........end  [s-t] or: [s-t] start.........end
        if s > end or t < start:
            continue
        if s < start: # [s--start-----?t].end  ?t]
            rs += [(s, start - 1), (start + delta, min(end, t) + delta)]
        else: # start.[s--?t].end  ?t]
            rs += [(s + delta, min(end, t) + delta)]

        # start.[s--t]..end
        if end > t: return rs   
        s = end
    if not rs: rs = [(s, t)]
    return rs

def process2(p):
    r = [(p[0], p[0] + p[1])]
    for m in maps:
        rs = []
        for s, t in r:
            rs += lookup2(s, t, m)
        r = rs
    return min(rs)[0]

locations  = [reduce(lookup, maps, s) for s in seeds]
locations2 = [process2((seeds[i:i + 2])) for i in range(0, len(seeds), 2)]

print(f"Part1: {min(locations)}")
print(f"Part2: {min(locations2)}")