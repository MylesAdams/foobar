def answer(h, q):
    p = []
    num = 2**h - 1

    for x in q:
        p.append(find_parent(x, num, num))

    return p


def find_parent(value, high, num_values):
    # Check if at root of current subtree
    if (high == value):
        return -1

    # Check if in right subtree, else left subtree
    if (value >= high - num_values//2):
        parent = find_parent(value, high - 1, num_values // 2)
    else:
        parent = find_parent(value, high - num_values//2 - 1, num_values//2)

    # Return label if label was returned, else return current root
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