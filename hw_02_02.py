from collections import deque

def is_palindrome(s):
    # Підготовка рядка: видалення пробілів та переведення до нижнього регістру
    s = ''.join(e for e in s.lower() if e.isalnum())
    
    # Створення двосторонньої черги з символів рядка
    char_deque = deque(s)
    
    while len(char_deque) > 1:
        # Якщо символи на протилежних кінцях не співпадають, рядок не є паліндромом
        if char_deque.popleft() != char_deque.pop():
            return False
    # Якщо всі символи співпали, рядок є паліндромом
    return True

# Тестування функції
test_strings = ["Madam", "Racecar", "Hello", "Was it a car or a cat I saw?", "No lemon, no melon", "123321",
                "А баба на волі — цілована баба", "Уму – мінімуму"]

for test in test_strings:
    print(f"'{test}': {'Поліндром' if is_palindrome(test) else 'Не поліндром' }")
