# Zadanie 1
import math
from time import time, sleep
from random import randrange, random
from inspect import getfullargspec


def timeit_decorator(func):
    """Print the execution time of a function"""
    def wrapper(*args, **kwargs):
        start_time = time()
        rs = func(*args, **kwargs)
        end_time = time()
        print(str((end_time-start_time)))
        return rs
    return wrapper


@timeit_decorator
def long_exec_func():
    sleep(0.01)


long_exec_func()


# Zadanie 2


tree = ["1", ["2", ["4", ["8", None, None], ["9", None, None]], ["5", None, None]],
        ["3", ["6", None, None], ["7", None, None]]]


def generate_tree(height: int):
    """Generate random binary tree of given height"""
    return generate_tree_rec(height-1, height-1, True)


def generate_tree_rec(height: int, current_height: int, leftmost: bool):
    if current_height == 0:
        value = randrange(0, 100)
        left_node = randrange(0, 100) if randrange(0, 2) == 1 else None
        right_node = randrange(0, 100) if randrange(0, 2) == 1 else None
        return [value, left_node, right_node]
    else:
        value = randrange(0, 100)
        if random() > 1/(current_height+1):
            left_node = generate_tree_rec(height, current_height - 1, False)
        else:
            left_node = None
        if random() > 1/(current_height+1):
            right_node = generate_tree_rec(height, current_height - 1, False)
        else:
            right_node = None
        if leftmost:
            left_node = generate_tree_rec(height, current_height - 1, True)
        return [value, left_node, right_node]


a = generate_tree(1)
print(a)


def dfs(tree_):
    for subtree in tree_:
        if isinstance(subtree, list):
            value, left, right = subtree
            yield value
            if left is not None and isinstance(left, list):
                yield from dfs(left)
            else:
                yield left
            if right is not None and isinstance(left, list):
                yield from dfs(right)
            else:
                yield right
        else:
            yield subtree


for i in dfs(a):
    print(i)


def bfs(tree_):
    stack = [tree_]
    while len(stack) > 0:
        if isinstance(stack[-1], list):
            value, left, right = list(stack.pop())
            yield value
            stack.insert(0, left)
            stack.insert(0, right)
        else:
            yield stack.pop()


for i in bfs(a):
    print(i)


# Zadanie 3

class Node(object):
    def __init__(self, value, subtrees=None):
        self.value = value
        self.subtrees = subtrees

    def __str__(self):
        rs = ""
        if isinstance(self.subtrees, list):
            for i in self.subtrees:
                rs += str(i) + " "
            return "[" + str(self.value) + ": " + rs + "]"
        else:
            return str(self.value)


def generate_tree_node(height: int):
    """Generate random binary tree of given height"""
    return generate_tree_rec_node(height-1, height-1, True)


def generate_tree_rec_node(height: int, current_height: int, leftmost: bool):
    if current_height == 0:
        value = randrange(0, 100)
        left_node = randrange(0, 100) if randrange(0, 2) == 1 else None
        right_node = randrange(0, 100) if randrange(0, 2) == 1 else None
        return Node(value, [Node(left_node), Node(right_node)])
    else:
        value = randrange(0, 100)
        if random() > 1/(current_height+1):
            left_node = generate_tree_rec_node(height, current_height - 1, False)
        else:
            left_node = None
        if random() > 1/(current_height+1):
            right_node = generate_tree_rec_node(height, current_height - 1, False)
        else:
            right_node = None
        if leftmost:
            left_node = generate_tree_rec_node(height, current_height - 1, True)
        return Node(value, [left_node, right_node])


b = generate_tree_node(2)
print(b)


def dfs_node(tree_: Node):
    yield tree_.value
    if tree_.subtrees is not None:
        for subtree in tree_.subtrees:
            if subtree is not None:
                yield from dfs_node(subtree)


print("DFS NODE")
for i in dfs_node(b):
    print(i)


def bfs_node(tree_):
    stack = [tree_]
    while len(stack) > 0:
        while not isinstance(stack[-1], Node):
            yield stack.pop()
        if isinstance(stack[-1], Node):
            node = stack.pop()
            value = node.value
            if isinstance(node.subtrees, list):
                for i in node.subtrees:
                    stack.insert(0, i)
            yield value


print("BFS NODE")
for i in bfs_node(b):
    print(i)

# Zadanie 4

print("------------------")


class OverLoader:
    funcs = {}

    def addFunc(self, func):
        self.funcs[len(getfullargspec(func).args)] = func

    def __call__(self, *args, **kwargs):
        total = len(args) + len(kwargs)
        return self.funcs[total](*args, **kwargs)


def overload(func):
    a = OverLoader()
    a.addFunc(func)
    return a


@overload
def norm(x, y):
    return math.sqrt(x * x + y * y)


@overload
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)


print(f"norm(2,4) = {norm(2, y=4)}")
print(f"norm(2,3,4) = {norm(2, 3, 4)}")
