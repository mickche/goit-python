all_words = ['monkey','programmer','engineer','Denis_Minka','water',]
n = 6

# 1.
def find_words(all_words,n):
    long_list = []
    for word in all_words:
        if len(word) > n:
            long_list.append(word)
    print(f"Список слів, довших за {n}: {long_list} ")
# find_words(all_words,n)

# 2.
def find_words2(all_words,n):
    long_list = [word for word in all_words if len(word) > n]
    print(f"Список слів, довших за {n}: {long_list} ")
find_words2(all_words,n)

s = input('Enter I, V, X, L, C, D і or M: ')
def romanToInt(s: str) -> int:
    rim_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    n = len(s)
    for i in range(n - 1):
        current_value = rim_map[s[i]]
        next_value = rim_map[s[i+1]]
        if current_value < next_value:
            result -= current_value
        else:
            result += current_value
    if n > 0:
        result += rim_map[s[n-1]]
    return result
print(f'Roman to int: {romanToInt(s)}')