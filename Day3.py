import time
import re
input = open("Day3Input.txt", "r")
''''
# Part 1
start = time.time()
for _ in range(1):
    input.seek(0)
    prev = input.readline()
    line = input.readline()
    next = input.readline()
    total = 0
    # First line
    nums = [[match.start(), match.end(), int(match.group(0))] for match in re.finditer(r'(\d+)', prev)]
    syms = [line[max(match[0]-1, 0):min(match[1]+1, len(line))] + prev[max(match[0]-1, 0)] + prev[match[1]] for match in nums]
    for i, num in enumerate(nums):
        if re.search(r'([^\d\.\n])', syms[i]) is None:
            continue
        else:
            total += num[2]
    # Middle lines
    while next:
        nums = [[match.start(), match.end(), int(match.group(0))] for match in re.finditer(r'(\d+)', line)]
        syms = [prev[max(match[0]-1, 0):min(match[1]+1, len(prev))] + next[max(match[0]-1, 0):min(match[1]+1, len(next))] + line[max(match[0]-1, 0)] + line[match[1]] for match in nums]
        for i, num in enumerate(nums):
            if re.search(r'([^\d\.\n]+)', syms[i]) is None:
                continue
            else:
                total += num[2]
        prev = line
        line = next
        next = input.readline()
    # Last line
    nums = [[match.start(), match.end(), int(match.group(0))] for match in re.finditer(r'(\d+)', line)]
    syms = [prev[max(match[0]-1, 0):min(match[1]+1, len(prev))] + line[max(match[0]-1, 0)] + line[match[1]] for match in nums]
    for i, num in enumerate(nums):
        if re.search(r'([^\d\.\n])', syms[i]) is None:
            continue
        else:
            total += num[2]
end = time.time()
print(end - start)
print(total)'''

def put_gear(gears, pos, part):
    if pos in gears:
        gears[pos].append(part)
    else:
        gears[pos] = [part]

def find_gear(gears, match, prev, line, next, line_num):
    l_bound = max(match[0]-1, 0)
    r_bound = min(match[1]+1, len(line))
    if prev is not None:
        top = prev[l_bound:r_bound]
        top_gears = [match.start() for match in re.finditer(r'\*{1}', top)]
        for gear in top_gears:
            pos = (min(match[0] + gear - len(top) + len(match[2]) + 1, r_bound - 1), line_num-1)
            put_gear(gears, pos, int(match[2]))
    if next is not None:
        bottom = next[l_bound:r_bound]
        bottom_gears = [match.start() for match in re.finditer(r'\*{1}', bottom)]
        for gear in bottom_gears:
            pos = (min(match[0] + gear - len(bottom) + len(match[2]) + 1, r_bound - 1), line_num+1)
            put_gear(gears, pos, int(match[2]))
    left = line[l_bound]
    if left == '*':
        pos = (l_bound, line_num)
        put_gear(gears, pos, int(match[2]))
    right = line[r_bound - 1]
    if right == '*':
        pos = (r_bound - 1, line_num)
        put_gear(gears, pos, int(match[2]))

# Part 2
start = time.time()
for _ in range(100):
    input.seek(0)
    lines = input.readlines()
    gears = {}
    for i, line in enumerate(lines):
        prev = lines[i-1] if i > 0 else None
        next = lines[i+1] if i < len(lines)-1 else None
        matches = [[match.start(), match.end(), match.group(0)] for match in re.finditer(r'(\d+)', line)]
        for match in matches:
            find_gear(gears, match, prev, line, next, i)
    count = len(gears.values())
    gear_list = filter(lambda x: len(x) == 2, gears.values())
    gear_list = [val[0]*val[1] for val in gear_list]
    total = sum(gear_list)
end = time.time()
print(end - start)
print(total)