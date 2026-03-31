# Залізні Острови використовують шифрування. Напиши декоратор @iron_cipher(shift), який:
# - Шифрує рядковий результат функції (César cipher з заданим зсувом)
# - Логує кожен виклик: ім'я функції + аргументи (через print або logging)
# - Зберігає __name__ і __doc__ оригінальної функції
# - Підтримує будь-яку кількість аргументів через *args, **kwargs
from functools import wraps


# def iron_cipher(shift: int):
#     def wrapper(func):
#         @wraps(func)
#         def inner(*args, **kwargs):
#             print(f'[CALL] {func.__name__}{args, kwargs}')
#             arg_list = []
#             for arg in args:
#                 new_arg = ''.join(list(chr(ord(l) + shift) if l.isalpha() else l for l in arg))
#                 arg_list.append(new_arg)
#             for key in kwargs:
#                 kwargs[key] = ''.join(list(chr(ord(l) + shift) if l.isalpha() else l for l in kwargs[key]))
#             return func(*arg_list, **kwargs)
#         return inner
#     return wrapper

def iron_cipher(shift: int):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print(f'[CALL] {func.__name__}{args, kwargs}')

            result = func(*args, **kwargs)

            if isinstance(result, str):
                encrypted_result = ""
                for char in result:
                    if char.isalpha():
                        # Визначаємо початкову точку (A або a)
                        start = ord('A') if char.isupper() else ord('a')
                        # Формула Цезаря: зсув всередині 26 літер алфавіту
                        new_char = chr((ord(char) - start + shift) % 26 + start)
                        encrypted_result += new_char
                    else:
                        # Символи, що не є літерами (пробіли, знаки), залишаємо як є
                        encrypted_result += char
                return encrypted_result
            return result
        return inner
    return wrapper



@iron_cipher(shift=3)
def send_message(sender, text):
    """Send a secret message."""
    return f"{sender}: {text}"

res = send_message("Theon", text = "Attack at dawn")
print(res)
# Лог: [CALL] send_message('Theon', 'Attack at dawn')
# result == "Wkhrq: Dwwdfn dw gdzq"

print(send_message.__name__) # "send_message"
print(send_message.__doc__)  # "Send a secret message."