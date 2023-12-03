import time
input = open("Day2Input.txt", "r")
# Part 1
possible = {
    'red': 12,
    'green': 13,
    'blue': 14
}
start = time.time()
for _ in range(100):
    input.seek(0)
    line = input.readline()
    sum = 0
    while line:
        parts = line.split(':')
        game_id = int(parts[0][5:])
        game = parts[1].split(';')
        valid = True
        for round in game:
            round = round.split(',')
            colors = [hand.strip().split(' ') for hand in round]
            for color in colors:
                if int(color[0]) > possible[color[1]]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            sum += game_id
        line = input.readline()
end = time.time()
print(end - start)
print(sum)
# Part 2
start = time.time()
for _ in range(100):
    input.seek(0)
    line = input.readline()
    sum = 0
    while line:
        parts = line.split(':')
        game = parts[1].split(';')
        mins = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for round in game:
            round = round.split(',')
            colors = [hand.strip().split(' ') for hand in round]
            for color in colors:
                val = int(color[0])
                if val > mins[color[1]]:
                    mins[color[1]] = val
        power = mins['red'] * mins['green'] * mins['blue']
        sum += power
        line = input.readline()
end = time.time()
print(end - start)
print(sum)