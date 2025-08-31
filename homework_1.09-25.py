from copy import deepcopy

market = {
    1:{
        'name':'Apple',
        'q': 4,
        'p':10
    },
    2:{
        'name':'Apple2',
        'q': 6,
        'p':20
    }

}

your_dict_product = {}
balance = 100

print(f'Balance before = {balance} \n')
print("--- list of product ---")
for key, product in market.items():
    print(f"Id: {key}")
    print(f"Name: {product['name']}")
    print(f"Quantity: {product['q']} ")
    print(f"Prise: {product['p']} ")
    print('\n')

while True:
    try:
        a = int(input("Enter 1 to continue shopping, 2 chekout , 0 quit: "))
    except ValueError:
        continue
    if a == 1:
        while True:
            try:
                id_pr = int(input('Enter Id product: '))
            except ValueError:
                continue
            if id_pr in market:
                # print("product found")
                pr = market[id_pr]
                break
            else:
                print("product NOT found")
                continue

        if pr['q'] == 0:
            print('Product left :(\n')
            continue
        your_dict_product[id_pr] = deepcopy(pr)
        # print(your_dict_product)
        while True:
            try:
                q_want = int(input('Enter how many: '))
            except ValueError:
                continue
            if q_want <=0:
                continue

            if q_want > pr['q']:
                print(f"There is only {pr['q']} left :(")
                continue
            else:
                your_dict_product[id_pr]['q'] = q_want
                # print(f"{your_dict_product[id_pr]['q']=}")
                # print(your_dict_product[id_pr])
                market[id_pr]['q'] -= q_want
                # print(f"{your_dict_product[id_pr]['q']=}")
                break
    elif a == 2:
        purchases_count = len(your_dict_product)
        if purchases_count == 0:
            print('Come back again :)')
            break
        total = 0
        for product in your_dict_product.values():
            # print(f"{total=} {product=}")
            total += product['p'] * product['q']
        print(f'Your purchase costs = {total} UAH \n')
        if total <= balance:
            print('Payment successfull \n')
            balance -= total
        else:
            print('Payment NOT successfull \n')

            print(f'You owe US!!! {total - balance} \n')
            balance = 0

        print('Come back again :) \n')

        break
    elif a == 0:
        print('Quit...')
        break
    else:
        continue
print(f'Balance after = {balance}')
