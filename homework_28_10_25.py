# Ініціалізуємо словник для зберігання користувачів
users = {}

def register(users, name, password):
    if name in users:
        return f"Помилка: Користувач з іменем '{name}' вже існує!"
    else:
        users[name] = password
        return f"Успіх: Користувач '{name}' успішно зареєстрований."

def login(users, name, password):
    if name in users:
        if users[name] == password:
            return f"Успіх: Вхід користувача '{name}' виконано."
        else:
            return "Недійсний логін або пароль."
    else:
        return "Недійсний логін або пароль."

def show_users(users):
    if users:
        # Отримуємо лише ключі (імена)
        user_list = ", ".join(users.keys())
        return f"Зареєстровані користувачі: {user_list}"
    else:
        return "Немає зареєстрованих користувачів."
print("--- Реєстрація ---")
print(register(users, "Den", "1234"))
print(register(users, "Anna", "qwerty"))
print(register(users, "Petro", "secure_pass"))
print("\n--- Відображення користувачів ---")
print(show_users(users))
print("\n--- Спроби входу ---")
print(f"Den, 1234: {login(users, 'Den', '1234')}")
print(f"Anna, 12345: {login(users, 'Anna', '12345')}")
print(f"Igor, 9876: {login(users, 'Igor', '9876')}")
print(f"Petro, secure_pass: {login(users, 'Petro', 'secure_pass')}")