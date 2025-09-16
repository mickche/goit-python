def revert(num):
    r_i = str(num)
    if num < 0:
        a = r_i[1:][::-1]
        a ='-'+ a
        try:
            return int(a)
        except ValueError:
            print('Введіть ціле число')
    else:
        return int(r_i[::-1])
print(revert(-13.90))