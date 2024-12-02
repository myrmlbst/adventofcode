# alternate solution using a one-liner for part 1
print(len(list(filter(lambda rept: (sorted(rept) == rept or sorted(rept) == rept[::-1]) and all([1 <= abs(rept[i] - rept[i + 1]) <= 3 for i in range(len(rept) - 1)]), [list(map(int, l.split())) for l in open("input.txt").readlines()],))))

# this is exact same as before but refactored to be more readable
print(
    len(
        list(
            filter(
                lambda rept: (sorted(rept) == rept or sorted(rept) == rept[::-1])
                and all([1 <= abs(rept[i] - rept[i + 1]) <= 3 for i in range(len(rept) - 1)]),
                [list(map(int, l.split())) for l in open("input.txt").readlines()],
            )
        )
    )
)