import re

with open("input2.txt") as f:
    ls = f.read().strip().split("\n")

ns = [list(map(int, re.findall("\\d+", x))) for x in ls]

# part 1
def safe1(levels):
    return all(1 <= abs(n1 - n2) <= 3 for n1, n2 in zip(levels, levels[1:])) and (
            levels == sorted(levels) or levels == sorted(levels)[::-1]
    )

# part 2
def safe2(levels):
    return any(safe1(levels[:i] + levels[i + 1:]) for i in range(len(levels)))

# part 1 answer
print(sum(safe1(levels) for levels in ns))

# part 2 answer
print(sum(safe2(levels) for levels in ns))