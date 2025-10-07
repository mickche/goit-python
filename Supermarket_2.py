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
market_copy = deepcopy(market)
your_dict_product = {}
balance = 100

desired_purchases = [
    (1, 3),
    (3, 2),
    (4, 10)
]

def display_market_recursive(mkt_items):
    if not mkt_items:
        return
    id, prod = mkt_items[0]
    print(f"ID {id}: {prod['name']}, Кількість: {prod['q']}, Ціна: {prod['p']} UAH")
    display_market_recursive(mkt_items[1:])

def display_market(mkt):
    print("--- Доступні продукти (ID: Назва, Кількість, Ціна) ---")
    display_market_recursive(list(mkt.items()))
    print("-" * 35)

def process_purchase_recursive(purchases, current_market, cart):
    if not purchases:
        return current_market, cart
    item_id, q_want = purchases[0]
    remaining_purchases = purchases[1:]
    if item_id in current_market:
        product = current_market[item_id]
        q_available = product['q']
        q_to_buy = min(q_want, q_available)
        if q_to_buy > 0:
            print(f" Купуємо {q_to_buy} шт. {product['name']} (ID {item_id}).")
            cart[item_id] = deepcopy(product)
            cart[item_id]['q'] = q_to_buy
            current_market[item_id]['q'] -= q_to_buy
        else:
            print(f"Покупку {product['name']} (ID {item_id}). Немає в наявності.")
    else:
        print(f"Продукт з ID {item_id} не знайдено на ринку.")
    return process_purchase_recursive(remaining_purchases, current_market, cart)

def print_cart_details_recursive(items):
    if not items:
        return
    item_id, P = items[0]
    subtotal = P['p'] * P['q']
    print(f" - {P['name']} (ID {item_id}): {P['q']} x {P['p']} UAH = {subtotal} UAH")
    return print_cart_details_recursive(items[1:])

print(f'Баланс до = {balance} UAH \n')
display_market(market)
final_market, final_cart = process_purchase_recursive(desired_purchases, market_copy, your_dict_product)

def calculate_total_recursive(items_list):
    if not items_list:
        return 0
    P = items_list[0]

    subtotal = P['p'] * P['q']
    return subtotal + calculate_total_recursive(items_list[1:])
cart_values_list = list(final_cart.values())
total = calculate_total_recursive(cart_values_list)

print("\n--- Деталі покупки ---")
print_cart_details_recursive(list(final_cart.items()))

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