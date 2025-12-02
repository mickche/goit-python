import re
from datetime import datetime

# --- 1. КЛАСИ СУТНОСТЕЙ ---

class Transaction:
    """Представляє фінансовий запис (дохід, витрата, інвестиція)."""
    def __init__(self, amount, category, type, description, date=None):
        self.amount = amount
        self.category = category
        self.type = type
        self.description = description
        self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M")

    def __str__(self):
        sign = "+" if self.type in ["Дохід", "Інвестиція"] else "-"
        return (f"[{self.date}] {self.type} ({self.category}): "
                f"{sign}{self.amount:.2f} | Опис: {self.description}")

class Template:
    """Представляє шаблон регулярної транзакції."""
    def __init__(self, name, amount, category, type):
        self.name = name
        self.amount = amount
        self.category = category
        self.type = type

    def __str__(self):
        return f"Шаблон '{self.name}': {self.type} ({self.category}), Сума: {self.amount:.2f}"

class User:
    """Представляє користувача з роллю для контролю доступу."""
    def __init__(self, username, role):
        self.username = username
        self.role = role # 'Адміністратор', 'Користувач', 'Гість'

# --- 2. КЛАС ФІНАНСОВОГО МЕНЕДЖЕРА З ЛОГІКОЮ ---

class FinancialManager:
    def __init__(self):
        self.transactions = []
        self.templates = {} # {name: Template_object}
        self.users = {'admin': User('admin', 'Адміністратор'), 
                      'user': User('user', 'Користувач'), 
                      'guest': User('guest', 'Гість')}
        self.current_user = None
        
        # Словник для парсингу категорій
        self.category_keywords = {
            'Харчування': ['кава', 'їжа', 'обід', 'продукти', 'ресторан'],
            'Транспорт': ['бензин', 'автобус', 'метро', 'таксі', 'проїзд'],
            'Розваги': ['кіно', 'Netflix', 'спортзал', 'гра'],
            'Зарплата': ['зарплата', 'аванс', 'премія'],
            'Інвестиції': ['акції', 'крипта', 'фонд', 'інвестував'],
        }
        
        self.transaction_types = ["Дохід", "Витрата", "Інвестиція"]

    # --- СИСТЕМА ДО