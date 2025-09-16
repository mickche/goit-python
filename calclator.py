
while True:
    print("Dostypni operachii: +, -, *, /")
    try:
        num1 = int(input("Enter 1 num: "))
        dia = input("Enter opearachiy (+, -, *, /): ")
        num2 = int(input("Enter 2 num: "))
        if dia == '+':
            result = num1 + num2
            print(f"Pruklad: {num1} + {num2} = {result}")
            break
        elif dia == '-':
            if num1 < num2:
                print("num1 ne mae bytu menshe nish num2")
                continue
            else:
                result = num1 - num2
                print(f"Pruklad: {num1} - {num2} = {result}")
                break

        elif dia == '*':
            result = num1 * num2
            print(f"Pruklad: {num1} * {num2} = {result}")
            break
        elif dia == '/':
            if num2 == 0:
                print("Error: na 0 dilutu ne moshna.")
                continue
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
                break
        else:
            print("Error: nevidoma aperachia vedit: +, -, *, /.")
            continue
    except ValueError:
        print("Error: enter only integer number.")