import time

input = open("Day1Input.txt", "r")

line = input.readline()
# Part 1
digits = ['0','1','2','3','4','5','6','7','8','9']
sum = 0
while line:
    num = ''
    for char in line:
        if char in digits:
            num += char
            break
    for char in line[::-1]:
        if char in digits:
            num += char
            break
    sum += int(num)
    line = input.readline()
print(sum)
# Part 2 (slow)
words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
mapping = {words[i]: digits[i] for i in range(len(words))}
start = time.time()
for _ in range(100):
    input.seek(0)
    line = input.readline()
    sum = 0
    while line:
        num = ''
        word_occurs = [line.find(word) if line.find(word) != -1 else 10000 for word in words]
        digit_occurs = [line.find(digit) if line.find(digit) != -1 else 10000 for digit in digits]
        min_i = min(word_occurs)
        min_j = min(digit_occurs)
        if min_i < min_j:
            num += mapping[words[word_occurs.index(min_i)]]
        else:
            num += digits[digit_occurs.index(min_j)]

        word_occurs = [line.rfind(word) for word in words]
        digit_occurs = [line.rfind(digit) for digit in digits]
        max_i = max(word_occurs)
        max_j = max(digit_occurs)
        if max_i > max_j:
            num += mapping[words[word_occurs.index(max_i)]]
        else:
            num += digits[digit_occurs.index(max_j)]
        
        sum += int(num)
        line = input.readline()
end = time.time()
print(end - start)
print(sum)
# Part 2 (faster)
letters = {
        'z':['zero'],
        'o': ['one'],
        't': ['two', 'three'],
        'f': ['four', 'five'],
        's': ['six', 'seven'],
        'e': ['eight'],
        'n': ['nine']
    }
words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
mapping = {words[i]: digits[i] for i in range(len(words))}
start = time.time()
for _ in range(100):
    input.seek(0)
    line = input.readline()
    sum = 0
    while line:
        num = ''
        for i, char in enumerate(line):
            stop = False
            if char in digits:
                num += char
                break
            elif char in letters:
                for word in letters[char]:
                    j = line.find(word)
                    if j == i:
                        num += mapping[word]
                        stop = True
                        break
            if stop:
                break
        for i, char in enumerate(line[::-1]):
            stop = False
            if char in digits:
                num += char
                break
            elif char in letters:
                for word in letters[char]:
                    j = line.rfind(word)
                    if j == len(line) - i - 1:
                        num += mapping[word]
                        stop = True
                        break
            if stop:
                break
        sum += int(num)
        line = input.readline()
end = time.time()
print(end - start)
print(sum)