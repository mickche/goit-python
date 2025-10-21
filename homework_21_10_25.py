def simple_table_generator(data, headers=None):
    all_rows = []
    if headers:
        all_rows.append(headers)
    all_rows.extend(data)

    if not all_rows:
        print("Немає даних для відображення.")
        return
    num_cols = max(len(row) for row in all_rows)
    column_widths = [0] * num_cols
    for row in all_rows:
        for i, cell in enumerate(row):
            cell_str = str(cell)
            if i < num_cols:
                column_widths[i] = max(column_widths[i], len(cell_str))

    def print_row(row_data, is_header=False):
        row_output = ""
        for i in range(num_cols):
            cell_content = str(row_data[i]) if i < len(row_data) else ""
            width = column_widths[i]
            formatted_cell = f"{cell_content:<{width}}"
            row_output += f"  {formatted_cell}"

        print(row_output.strip())
    if headers:
        print_row(headers, is_header=True)
        separator_line = ""
        for width in column_widths:
            separator_line += f"  {'-' * width}"
        print(separator_line.strip())
    for row in data:
        print_row(row)
headers_ex = ["Ім'я", "Посада", "Зарплата"]
data_ex = [
    ["Іван", "Розробник", 60000],
    ["Ольга", "Менеджер Проєктів", 85000],
    ["Петро", "Аналітик", 52000]
]
print("--- Проста таблиця ---")
simple_table_generator(data_ex, headers_ex)