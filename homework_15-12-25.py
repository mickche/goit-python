import string
import itertools

# --- 1. Генератор простих чисел ---
def prime_generator():
    number = 2
    while True:
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            yield number
        number += 1

# --- 2. Генератор паролів ---
def password_generator(max_length):
    # Латинські літери нижнього регістру + цифри
    chars = string.ascii_lowercase + string.digits
    for length in range(1, max_length + 1):
        for combination in itertools.product(chars, repeat=length):
            yield ''.join(combination)

# --- 3. Спільні елементи двох списків ---
def common_elements_generator(list1, list2):
    seen = set()
    set2 = set(list2)
    for item in list1:
        if item in set2 and item not in seen:
            seen.add(item)
            yield item

# --- 4. Кумулятивна сума ---
def cumulative_sum_generator(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total


def csv_dict_generator(data):
    if not data:
        return
    headers = data[0]
    for row in data[1:]:
        yield dict(zip(headers, row))


if __name__ == "__main__":
    print("--- 1. Прості числа (перші 10) ---")
    primes = prime_generator()
    print([next(primes) for _ in range(10)])

    print("\n--- 2. Генератор паролів (перші 5 довжиною до 4) ---")
    pass_gen = password_generator(4)
    for _ in range(5):
        print(next(pass_gen))

    print("\n--- 3. Спільні елементи ---")
    list_a = [1, 2, 2, 3, 4, 10]
    list_b = [2, 4, 4, 5, 10]
    print(list(common_elements_generator(list_a, list_b)))

    print("\n--- 4. Кумулятивна сума ---")
    nums = [1, 2, 3, 4, 5]
    print(list(cumulative_sum_generator(nums)))

    print("\n--- 5. CSV як словник ---")
    csv_data = [
        ["id", "product", "price"],
        ["1", "Laptop", "1200"],
        ["2", "Mouse", "25"]
    ]
    for row in csv_dict_generator(csv_data):
        print(row)