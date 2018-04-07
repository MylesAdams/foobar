def answer(n, b):
    k = len(n)
    nums_seen = {}
    cur_num = n
    cycle_size = 1

    while (cur_num not in nums_seen):
        nums_seen[cur_num] = 1
        cur_num = calculate_z(cur_num, b, k)

    cycle_start = cur_num
    cur_num = calculate_z(cur_num, b, k)

    while (cur_num != cycle_start):
        cur_num = calculate_z(cur_num, b, k)
        cycle_size += 1

    return cycle_size


# Change from base 10 to any base -> Returns number backwords
def to_any_base(num, b):
    num_b = []
    to_any_base_recur(num_b, num, b)
    return num_b


# Recursive function for changing from base 10 to any base
def to_any_base_recur(num_b, num, b):
    num_b.append(str(num % b))
    new_num = num // b

    if new_num == 0:
        return

    to_any_base_recur(num_b, new_num, b)


# Change from base 10 to any base and prepend zeros to keep correct length -> Returns number normal
def change_base_and_fix_length(num, b, k):
    num_b = to_any_base(num, b)

    for i in range(len(num_b), k):
        num_b.append('0')

    return ''.join(num_b[::-1])


# Return digits of num in ascending order
def num_digits_in_ascending(num):
    return ''.join(sorted(num))


# Return digits of num in descending order
def num_digits_in_descending(num):
    return ''.join(sorted(num, reverse=True))


# Calculate z -> x and y start in base b, and z is returned in base b
def calculate_z(num, b, k):
    x = int(num_digits_in_descending(num), b)
    y = int(num_digits_in_ascending(num), b)

    z = x - y

    return change_base_and_fix_length(z, b, k)



print(oct(127))

print(int('30', 5))

print('9')

print(int('9') + 10)

print(change_base_and_fix_length(127, 7, 10))

print(num_digits_in_ascending("54768123"))

print(num_digits_in_descending("54768123"))

print(answer("1211", 10))

print(answer("210022", 3))