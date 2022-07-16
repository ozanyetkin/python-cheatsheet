with open('11_advent_of_code/day_10.txt') as f:
    lines = f.readlines()

data = [l.replace("\n", "") for l in lines]

def corrupt(input_string, pos=0, open_list=[]):
    if input_string[pos] in ["(", "[", "{", "<"]:
        open_list.append(input_string[pos])
        pos += 1
        return corrupt(input_string, pos, open_list)
    else:
        if input_string[pos] == ")":
            if open_list[-1] != "(":
                return 3
        if input_string[pos] == "]":
            if open_list[-1] != "[":
                return 57
        if input_string[pos] == "}":
            if open_list[-1] != "{":
                return 1197
        if input_string[pos] == ">":
            if open_list[-1] != "<":
                return 25137
    open_list.pop()
    pos += 1
    return corrupt(input_string, pos, open_list)

def incomplete(input_string, pos=0, open_list=[]):
    if input_string[pos] in ["(", "[", "{", "<"]:
        open_list.append(input_string[pos])
        if pos == len(input_string) - 1:
            return open_list
        pos += 1
        return incomplete(input_string, pos, open_list)
    else:
        if input_string[pos] == ")":
            if open_list[-1] != "(":
                raise ValueError
        if input_string[pos] == "]":
            if open_list[-1] != "[":
                raise ValueError
        if input_string[pos] == "}":
            if open_list[-1] != "{":
                raise ValueError
        if input_string[pos] == ">":
            if open_list[-1] != "<":
                raise ValueError
    open_list.pop()
    if pos == len(input_string) - 1:
        return open_list
    pos += 1
    return incomplete(input_string, pos, open_list)

score_list = []
for line in data:
    try:
        score = 0
        incomplete_chars = incomplete(line, pos=1, open_list=[line[0]])
        incomplete_chars.reverse()
        for char in incomplete_chars:
            score *= 5
            if char == "(":
                score += 1
            if char == "[":
                score += 2
            if char == "{":
                score += 3
            if char == "<":
                score += 4
        score_list.append(score)
    except ValueError:
        pass

score_list.sort()
print(score_list[len(score_list) // 2])
