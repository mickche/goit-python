from copy import deepcopy

market = {
    1: {
        'name': 'Apple',
        'q': 4,
        'p': 10},
    2: {'name': 'Apple2',
        'q': 6,
        'p': 20
        },
    3: {'name': 'Pear',
        'q': 4,
        'p': 12
        },
    4: {'name': 'Banana',
        'q': 6,
        'p': 7,
        }
}
your_dict_product = {}
balance = 100

desired_purchases = [
    (1, 3),
    (3, 2),
    (4, 10)
]


def display_market(mkt):
    print("--- Доступні продукти (ID: Назва, Кількість, Ціна) ---")
    for id, prod in mkt.items():
        print(f"ID {id}: {prod['name']}, Кількість: {prod['q']}, Ціна: {prod['p']} UAH")
    print("-" * 35)


def process_purchase_recursive(purchases, current_market, cart):
    if not purchases:
        return current_market, cart

    item_id, q_want = purchases[0]

    if item_id in current_market:
        product = current_market[item_id]

        q_to_buy = min(q_want, product['q'])

        if q_to_buy > 0:
            print(f" Купуємо {q_to_buy} шт. {product['name']} (ID {item_id}).")

            cart[item_id] = deepcopy(product)
            cart[item_id]['q'] = q_to_buy

            current_market[item_id]['q'] -= q_to_buy
        else:
            print("Покупку {product['name']} (ID {item_id}). Немає в наявності.")
    else:
        print(f"Продукт з ID {item_id} не знайдено на ринку.")

    return process_purchase_recursive(purchases[1:], current_market, cart)



print(f'Баланс до = {balance} UAH \n')

display_market(market)

final_market, final_cart = process_purchase_recursive(desired_purchases, market, your_dict_product)

total = 0
print("--- Деталі покупки ---")
for id, P in final_cart.items():
    subtotal = P['p'] * P['q']
    total += subtotal
    print(f" - {P['name']} (ID {id}): {P['q']} x {P['p']} UAH = {subtotal} UAH")

print(f'\nВартість покупки = {total} UAH')


if total <= balance:
    print('Оплата успішна!')
    balance -= total
else:
    print(' Оплата НЕ успішна!')

    print(f'Ви нам винні {total - balance} UAH')
    balance = 0

print('\nЗаходьте ще :)')
print(f'Баланс після = {balance} UAH')

display_market(final_market)