from collections import defaultdict

with open("input5.txt") as f:
    raw_rules, updates = f.read().strip().split("\n""\n")
    rules = []
    for line in raw_rules.split("\n"):
        a, b = line.split("|")
        rules.append((int(a), int(b)))
    updates = [list(map(int, line.split(","))) for line in updates.split("\n")]

def follows_rules(update):
    idx = {}
    for i, num in enumerate(update):
        idx[num] = i
    for a, b in rules:
        if a in idx and b in idx and not idx[a] < idx[b]:
            return False, 0
    return True, update[len(update) // 2]


# part 1
ans = 0
for update in updates:
    good, mid = follows_rules(update)
    if good:
        ans += mid

print(ans)


# part 2
def sort_correctly(update):
    my_rules = []
    for a, b in rules:
        if not (a in update and b in update):
            continue
        my_rules.append((a, b))

    indegree = defaultdict(int)
    for a, b in my_rules:
        indegree[b] += 1

    ans = []
    while len(ans) < len(update):
        for x in update:
            if x in ans:
                continue
            if indegree[x] <= 0:
                ans.append(x)
                for a, b in my_rules:
                    if a == x:
                        indegree[b] -= 1
    return ans

ans = 0
for update in updates:
    if follows_rules(update)[0]:
        continue
    seq = sort_correctly(update)
    ans += seq[len(seq) // 2]

print(ans)