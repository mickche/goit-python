import functools
import time
from typing import List, Callable, Generator, Any, Type, Tuple

# --- 1. Анотація типів для функції суми ---

def add_numbers(a: int, b: int) -> int:
    """Приймає два цілі числа та повертає їх суму."""
    return a + b

# --- 2. Функція замикання для генератора послідовностей ---

def sequence_generator_factory(start: int, step: int) -> Callable[[], Generator[int, None, None]]:
    """
    Створює та повертає функцію-генератор, яка генерує арифметичну послідовність.
    """
    current_value = start
    
    def generator() -> Generator[int, None, None]:
        """Генератор послідовності."""
        nonlocal current_value
        while True:
            yield current_value
            current_value += step
            
    return generator

# --- 3. Декоратор для логування аргументів та результату ---

def log_call(func: Callable) -> Callable:
    """Декоратор, що логує аргументи, з якими була викликана функція, та її результат."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        
        print(f"-> [LOG] Викликана функція {func.__name__} з аргументами: ({signature})")
        
        result = func(*args, **kwargs)
        
        print(f"<- [LOG] Функція {func.__name__} повернула результат: {result!r}")
        
        return result
    return wrapper

# --- 4. Замикання для логування кількості викликів ---

def call_counter() -> Callable[[Callable], Callable]:
    """Створює замикання-декоратор для логування кількості викликів функції."""
    count = 0
    
    def decorator(func: Callable) -> Callable:
        nonlocal count
        
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            nonlocal count
            count += 1
            print(f"[COUNT] Функція {func.__name__} була викликана {count} раз(ів).")
            return func(*args, **kwargs)
        return wrapper
        
    return decorator