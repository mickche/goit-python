import random
def generate_code():
    digits = list("0123456789")
    random.shuffle(digits)
    code = "".join(digits[:3])

    while code[0] == '0' or len(set(code)) != 3:
        random.shuffle(digits)
        code = "".join(digits[:3])

    return code

def check_guess(secret_code, guess):
    correct_position = 0
    correct_digit_wrong_position = 0

    for i in range(len(secret_code)):
        if secret_code[i] == guess[i]:
            correct_position += 1
    for i in range(len(guess)):
        digit = guess[i]
        if digit in secret_code and secret_code[i] != digit:
            correct_digit_wrong_position += 1

    return correct_position, correct_digit_wrong_position

def play_game():
    print("----- Гра 'Кодовий Замок'-----")
    print("Мета: Вгадати 3-значний код із неповторюваних цифр.")
    print("Підказки:")
    print("Правильне місце: Цифра стоїть на правильному місці.")
    print("Правильна цифра: Цифра є в коді, але на іншому місці.")

    secret_code = generate_code()
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        attempts += 1

        guess = input(f"\nСпроба #{attempts}. Введіть 3-значний код: ")

        if len(guess) != 3 or not guess.isdigit() or len(set(guess)) != 3:
            print(" Неправильний формат. Введіть рівно 3 **неповторювані** цифри.")
            continue

        correct_pos, correct_digit_wrong_pos = check_guess(secret_code, guess)

        if correct_pos == 3:
            print(f"\nКОД ЗНАЙДЕНО! Ви розгадали код '{secret_code}' за {attempts} спроб!")
            break
        print(f"Підказка:")
        print(f"На правильних місцях: {correct_pos}")
        print(f"Є в коді (на інших місцях): {correct_digit_wrong_pos}")

        if attempts == max_attempts:
            print(f"\nСпроби вичерпано. Код був '{secret_code}'.")

if __name__ == "__main__":
    play_game()