## part 1:
print(sum(map(lambda t: abs(t[0][0] - t[1][1]), zip(sorted(x := [list(map(int, l.split())) for l in open("input.txt").readlines()],key=lambda y: y[0]), sorted(x, key=lambda y:y[1])))))

## part 2:
print(sum(map(lambda e: sum([e[0] == x[1] for x in pr])*e[0], (pr := [list(map(int, l.split())) for l in open("input.txt").readlines()]))))


'''
# below is the same code, refactored to be less ugly/more readable

# part 1:
print(sum(\
    map(\
        lambda t: abs(t[0][0] - t[1][1]),\
         zip(sorted(x := [list(map(int, l.split())) \
                          for l in open("input.txt").readlines()],\
                key=lambda y: y[0]), \
            sorted(x, \
                key=lambda y:y[1]\
            ))\
        )\
    )\
)

## part 2:
print(sum(\
    map(lambda e: sum([e[0] == x[1] for x in pr])*e[0], \
        (pr := [list(map(int, l.split())) \
                for l in open("input.txt").readlines()]\
        )\
    )\
))
'''