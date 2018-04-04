# def answer(h, q):
#     p = []
#     tree = [None] * (2**h - 1)
#     build_tree(tree, 1, 2**h-1, 0)
#     print(tree)
#
#     for x in q:
#         parent_index = (tree.index(x) - 1)//2
#         if parent_index >= 0:
#             p.append(tree[parent_index])
#         else:
#             p.append(-1)
#
#     return p


def answer(h, q):
    p = []
    num = 2**h - 1

    for x in q:
        p.append(find_parent(x, num, num))

    return p


def build_tree(tree, low, num_values, index):
    tree[index] = low + num_values - 1
    if num_values != 1:
        build_tree(tree, low, num_values//2, 2*index + 1)
        build_tree(tree, low + num_values//2, num_values//2, 2*index + 2)


def find_parent(value, high, num_values):
    if (high == value):
        return -1

    if (value >= high - num_values//2):
        parent = find_parent(value, high - 1, num_values // 2)
    else:
        parent = find_parent(value, high - num_values//2 - 1, num_values//2)

    return parent if (parent != -1) else high


print()

ans = answer(3, [7, 3, 5, 1])
print(ans)

print()

ans = answer(5, [19, 14, 28])
print(ans)

print()

ans = answer(30, [19, 14, 28])
print(ans)