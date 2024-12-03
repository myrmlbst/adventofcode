# alternate solution using one-liners

# part 1
print(len(list(filter(lambda rept: (sorted(rept) == rept or sorted(rept) == rept[::-1]) and all([1 <= abs(rept[i] - rept[i + 1]) <= 3 for i in range(len(rept) - 1)]), [list(map(int, l.split())) for l in open("input2.txt").readlines()],))))

# part 2: problem dampening
print(len(list(filter(lambda rept: any((sorted((re := rept[:j] + rept[j + 1 :])) == re or sorted(re) == re[::-1]) and all([1 <= abs(re[i] - re[i + 1]) <= 3 for i in range(len(re) - 1)]) for j in range(len(rept))), [list(map(int, l.split())) for l in open("input2.txt").readlines()],))))
