import random
secret_number = random.randint(1, 100)

def number():
    print("Я загадав число від 1 до 100. Спробуй вгадати!")
    while True:
        try:
            guess = int(input("Введіть ваше число: "))
        except ValueError:
            print("Введіть ціле число.")
            continue
        # print("Гарна спроба!" if 1 <= guess <= 100 else "Спробуй ще!")

        # if 1 <= guess <= 100:
        #     print("Гарна спроба!")
        # else:
        #     print("Спробуй ще!")

        if guess < secret_number:
            print("Трішки більше...")
        elif guess > secret_number:
            print("Трішки менше...")
        else:
            print("Вітаю! Ви розкрили секрет!")
            break

def main():
    # number()
    print()

if __name__ == main():
    main()
