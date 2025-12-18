import math
import copy
from collections import defaultdict


def task_1():
    my_tuple = ("Python", 2024, (1, 2, 3), 3.14, True)
    return {item: type(item).__name__ for item in my_tuple}


def task_2(nums):
    if not nums: return None
    mini = maxi = nums[0]
    for n in nums:
        if n < mini: mini = n
        if n > maxi: maxi = n
    return mini, maxi


def task_3(matrix_tuple):
    return tuple(sub[1] for sub in matrix_tuple)


def task_4(text):
    vowels = "aeiouyаеєиіїоуюя"
    v_count = c_count = 0
    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return (v_count, c_count)


def task_5(nums):
    return round(sum(nums) / len(nums), 2) if nums else 0


def task_6(matrix):
    return [tuple(row) for row in zip(*matrix)]


def task_7(t1, t2):
    return tuple(x for x in t1 if x in t2)


def task_8(data):
    strings = tuple(sorted([x for x in data if isinstance(x, str)]))
    numbers = tuple(sorted([x for x in data if isinstance(x, (int, float))]))
    return strings, numbers


def task_9(*tuples):
    return tuple(min(t) for t in tuples if t)


def task_10(t):
    return tuple(x for x in t if t.count(x) == 1)


def task_11(people):
    if not people: return ()
    avg_age = sum(p[1] for p in people) / len(people)
    return tuple(p for p in people if p[1] > avg_age)


def task_12(text):
    return tuple((word, len(word)) for word in text.split())


def task_13(prices_list):
    d = defaultdict(list)
    for pid, price in prices_list:
        d[pid].append(price)
    return tuple((pid, sum(p) / len(p)) for pid, p in d.items())


def task_14(people_dates):
    return sorted(people_dates, key=lambda x: (x[1][1], x[1][2]))


def task_15(data):
    return copy.deepcopy(data)


def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True


def task_16(people, char):
    return [p for p in people if is_prime(p[1]) and p[2].lower().startswith(char.lower())]


def task_17(ts, t_type=None, date=None):
    if t_type: return [t for t in ts if t[2] == t_type]
    if date: return [t for t in ts if t[3] == date]
    return ts


def task_18(matrix, angle_rad):
    res = []
    for row in matrix:
        new_row = []
        for x, y, z in row:
            new_y = y * math.cos(angle_rad) - z * math.sin(angle_rad)
            new_z = y * math.sin(angle_rad) + z * math.cos(angle_rad)
            new_row.append((x, round(new_y, 2), round(new_z, 2)))
        res.append(tuple(new_row))
    return res


if __name__ == "__main__":
    t1_res = task_1()
    t2_res = task_2((10, 5, 22, 1, 18))
    t3_res = task_3(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
    t4_res = task_4("Hello Python")
    t5_res = task_5((10, 20, 33))
    t6_res = task_6([(1, 2, 3), (4, 5, 6)])
    t7_res = task_7((1, 2, 3), (2, 3, 4))
    t8_res = task_8(("apple", 10, "banana", 5))
    t9_res = task_9((1, 2), (5, 0), (10, 8))
    t10_res = task_10((1, 2, 2, 3, 4, 4, 5))
    t11_res = task_11((("Ivan", 25, "Dev"), ("Anna", 35, "PM"), ("Oleg", 20, "QA")))
    t12_res = task_12("Python is great")
    t13_res = task_13([(1, 100), (2, 200), (1, 150)])
    t14_res = task_14([("Ivan", (1990, 12, 5)), ("Anna", (1995, 1, 20))])
    t15_res = task_15([(1, (2, 3))])
    t16_res = task_16([("Oleh", 23, "Designer"), ("Maria", 24, "Doctor")], "D")

    transactions = [(1, 100.0, "income", "2023-10-01"), (2, 50.0, "expense", "2023-10-02")]
    t17_res = task_17(transactions, t_type="income")

    coords = [[(1, 0, 0), (0, 1, 0)]]
    t18_res = task_18(coords, math.pi / 2)