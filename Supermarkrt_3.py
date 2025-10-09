# Це 3 версія :)
def find_product(product_name, storage, i=0):
    if i == len(storage):
        return None
    elif storage[i][0] == product_name:
        return storage[i]
    else:
        return find_product(product_name, storage, i + 1)
def print_storage(storage, i=0):
    if i == len(storage):
        return None
    print(f"{i+1}. {storage[i][0]} - {storage[i][1]}")
    return print_storage(storage, i + 1)
def shop_loop(storage, pocket, shop_name):
    print(f"Магазин: {shop_name}")
    print("1. Додати товар")
    print("2. Видалити товар")
    print("3. Купити товар")
    print("4. Перегляд списку товарів")
    print("5. Перегляд балансу")
    print("6. Вийти")
    option = input("Введіть функцію числом (1-6): ")
    print()
    if option == "1":
        print("Додавання товару")
        product_name = input("Введіть назву товару: ")
        product_price = int(input("Введіть ціну товару: "))
        product = [product_name, product_price]
        storage.append(product)
        print(f"Товар '{product_name}' додано.")
    elif option == "2":
        print("Видалення товару")
        product_name = input("Введіть назву товару для видалення: ")
        product = find_product(product_name, storage)
        if product:
            storage.remove(product)
            print(f"Товар '{product_name}' видалено.")
        else:
            print(f"Товар '{product_name}' не знайдено.")
    elif option == "3":
        print("Купівля товару")
        product_name = input("Введіть назву товару для покупки: ")
        product = find_product(product_name, storage)
        if product:
            pocket += product[1]
            storage.remove(product)
            print(f"Ви придбали '{product_name}'.")
        else:
            print(f"Товар '{product_name}' не знайдено.")
    elif option == "4":
        print("Перегляд товарів")
        if not storage:
            print("Список товарів порожній.")
        else:
            print_storage(storage)
    elif option == "5":
        print(f"Баланс магазину: {pocket}$")
    elif option == "6":
        print("Вихід з програми.")
        return None
    else:
        print("Такого варіанту немає :(")
    print()
    return shop_loop(storage, pocket, shop_name)
def main():
    return shop_loop(
        storage=[],
        pocket=0.0,
        shop_name="Ahan"
    )
if __name__ == '__main__':
    main()
