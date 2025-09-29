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