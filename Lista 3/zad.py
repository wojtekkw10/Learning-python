# Zadanie 1
from functools import reduce

matrix = ["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]


def transpose(matrix_):
    return [" ".join([j.split(" ")[i] for j in matrix_]) for i in range(0, len(matrix_))]


print(transpose(matrix))


# Zadanie 2

def flatten(l_):
    for i in l_:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i


my_list = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6 ], 7, [[9, [123, [[123]]]], 10]]
print(list(flatten(my_list)))

# Zadanie 3
print(reduce(lambda x, y: x+y, [int(j[0].split(" ")[-1]) for j in [i.splitlines() for i in open("plik")]]))


# Zadanie 4

def qsort(list_):
    if len(list_) == 0:
        return []
    elif len(list_) == 1:
        return list_
    else:
        return [qsort(list(filter(lambda x: x < k, list_)))
                + [k]
                + qsort(list(filter(lambda x: x >= k, list_)))
                for k in [list_.pop(0)]][0]


list2 = [2, 3, 1, 7, 3, 4, 2]
print(qsort(list2))


def allsubsets(list_):
    if len(list_) == 0:
        return [[]]
    else:
        a = list_.pop(0)
        res = allsubsets(list_)
        return list(map(lambda l: [a] + l, res)) + res


print(allsubsets(list(range(1, 4))))
