import random
def generateList(n):
    l = [x for x in range(n)]
    random.shuffle(l)
    return l


def right_order(l):
    for i, v in enumerate(l):
        if v != i:
            return False
    return True


def find_cycles(l):
    v = set()
    cycles = []
    for i in range(len(l)):
        curr_cycle = []
        if i not in v:
            curr = i
            # input("continue:")
            while curr not in v:
                curr_cycle.append(curr)
                v.add(curr)
                curr = l[curr]
            if len(curr_cycle) > 1:
                cycles.append(curr_cycle)
    # print("Cycles of the bsets)
    misplaced = 0
    for i, val in enumerate(l):
        if i != val:
            misplaced += 1
    zero_cycle = 0
    for s in cycles:
        if 0 in s:
            zero_cycle = 2

    return misplaced + len(cycles) - zero_cycle


def solve(oldl):
    original = oldl.copy()
    prediction = find_cycles(oldl)
    steps = 0
    resets = 0
    while not right_order(oldl):
        for i in range(len(oldl)):
            if oldl[0] == 0:
                if 0 < i != oldl[i]:
                    swap = 0
                    oldl[i], oldl[swap] = oldl[swap], oldl[i]
                    steps += 1
                    resets += 1
                    break
            else:
                if oldl[i] == 0 and i != 0:
                    swap = oldl.index(i)
                    oldl[i], oldl[swap] = oldl[swap], oldl[i]
                    steps += 1
                    break
    return original, prediction, steps


if __name__ == '__main__':
    for i in range(120):
        l = generateList(10)
        og, prediction, numsteps = solve(l)
        print("List: ", og, "Prediction: ", prediction, "Actual:", numsteps)