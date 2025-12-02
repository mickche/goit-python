# ===============================================
# === ФУНКЦІЇ ДЛЯ КОЖНОГО ЗАВДАННЯ (1-18) ===
# ===============================================
# 1. Словник типів даних
def create_type_dictionary(data_tuple):
    result_dict = {}
    for item in data_tuple:
        result_dict[item] = type(item).__name__
    return result_dict

# 2. Знаходження min/max без вбудованих функцій
def find_min_max(numbers_tuple):
    if not numbers_tuple:
        return None, None
    current_min = numbers_tuple[0]
    current_max = numbers_tuple[0]
    for number in numbers_tuple[1:]:
        if number < current_min:
            current_min = number
        if number > current_max:
            current_max = number
    return current_min, current_max

# 3. Витягнення других елементів з кортежів
def extract_second_elements(tuple_of_tuples):
    new_tuple = [sub_tuple[1] for sub_tuple in tuple_of_tuples if len(sub_tuple) >= 2]
    return tuple(new_tuple)

# 4. Аналіз голосних та приголосних
def analyze_text_vowels_consonants(text):
    vowels_set = {'А', 'Е', 'Є', 'И', 'І', 'Ї', 'О', 'У', 'Ю', 'Я'}
    vowel_count = 0
    consonant_count = 0
    processed_text = text.upper()
    
    for char in processed_text:
        if 'А' <= char <= 'Я':
            if char in vowels_set:
                vowel_count += 1
            else:
                consonant_count += 1
                
    return (vowel_count, consonant_count)

# 5. Обчислення та округлення середнього
def calculate_average_and_round(numbers_tuple):
    if not numbers_tuple:
        return 0.0
    total_sum = sum(numbers_tuple)
    average = total_sum / len(numbers_tuple)
    return round(average, 2)

# 6. Транспонування матриці (список кортежів)
def transpose_matrix(matrix_rows):
    if not matrix_rows or not matrix_rows[0]:
        return []

    num_rows = len(matrix_rows)
    num_cols = len(matrix_rows[0])
    transposed_matrix = []
    
    for col_index in range(num_cols):
        new_row = [matrix_rows[row_index][col_index] for row_index in range(num_rows)]
        transposed_matrix.append(tuple(new_row))
        
    return transposed_matrix

# 7. Знаходження спільних елементів (перетин)
def find_common_elements(tuple1, tuple2):
    common_elements_set = set(tuple1).intersection(set(tuple2))
    return tuple(common_elements_set)

# 8. Сортування рядків за алфавітом, чисел за зростанням
def sort_strings_and_numbers(data_tuple):
    strings = []
    numbers = []
    
    for item in data_tuple:
        if isinstance(item, str):
            strings.append(item)
        elif isinstance(item, (int, float)):
            numbers.append(item)
            
    return (tuple(sorted(strings)), tuple(sorted(numbers)))

# 9. (та 10.) Кортеж найменших елементів із вхідних кортежів
def get_min_elements_from_tuples(*tuples):
    min_elements = []
    for current_tuple in tuples:
        if current_tuple:
            min_elements.append(min(current_tuple))
    return tuple(min_elements)

# 11. Елементи, що зустрічаються лише один раз
def find_singly_occurring_elements(input_tuple):
    element_counts = Counter(input_tuple)
    unique_elements = [item for item, count in element_counts.items() if count == 1]
    return tuple(unique_elements)

# 12. Кортеж (Слово, Довжина)
def create_word_length_tuples(text):
    # Потребує import re
    words = re.findall(r'\b[а-яА-ЯёЁa-zA-ZіІїЇєЄ]+\b', text)
    word_length_list = [(word, len(word)) for word in words]
    return tuple(word_length_list)

# 13. Середня ціна продукту
def calculate_average_price(product_list):
    price_data = defaultdict(lambda: {'sum': 0.0, 'count': 0})
    
    for product_id, price in product_list:
        price_data[product_id]['sum'] += price
        price_data[product_id]['count'] += 1
        
    result_list = []
    for product_id, data in price_data.items():
        average_price = data['sum'] / data['count'] if data['count'] > 0 else 0.0
        result_list.append((product_id, round(average_price, 2)))
        
    return tuple(result_list)

def sort_by_month_then_day(person_list):
    sort_key = lambda item: (item[1][5:7], item[1][8:10])
    sorted_list = sorted(person_list, key=sort_key)
    return sorted_list

# 15. Глибоке копіювання списку кортежів
def deep_copy_tuple_list(list_of_tuples):
    return copy.deepcopy(list_of_tuples)

# 16. Фільтрація за простим віком та першою літерою професії
def filter_records(records, starting_letter):
    target_letter = starting_letter.upper()
    filtered_list = []
    
    for name, age, profession in records:
        is_age_prime = is_prime(age)
        is_profession_match = (profession and profession[0].upper() == target_letter)
        
        if is_age_prime and is_profession_match:
            filtered_list.append((name, age, profession))
            
    return filtered_list

# 17. Фільтрація транзакцій за типом та датою
def filter_transactions(transactions, target_type, target_date=None):
    filtered_transactions = []
    for tx_id, amount, tx_type, tx_date in transactions:
        if tx_type == target_type:
            if target_date is None or tx_date == target_date:
                filtered_transactions.append((tx_id, amount, tx_type, tx_date))
                
    return filtered_transactions

# 18. Обернена трансформація (матричні операції)
def apply_inverse_transformation(triplets_matrix, inverse_matrix):
    points_array = np.array(triplets_matrix) 
    transformed_points = points_array @ inverse_matrix
    
    result_list = [
        tuple(np.round(point, 4)) 
        for point in transformed_points
    ]
    
    return result_list