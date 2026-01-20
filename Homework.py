def More(func): #Декотор1 в наибольшую
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return round(result * 2.1, 2)
    return wrapper


def Less(func): #Декотор2 в наименьшую
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return round(result / 2.1, 2)
    return wrapper
@More
def add(a, b):
    """Складывает a и b"""
    return a + b

@More
def subtract(a, b):
    """Вычитает b из a"""
    return a - b

@More
def multiply(a, b):
    """Умножает a на b"""
    return a * b

@More
def divide(a, b):
    return a / b


print("Коэфицент 2.1 в большую сторону")
print(add(3, 4)) # значение чисел которые будут складываться
print(subtract(8, 3)) # значение чисел которые будут уменьшаться
print(multiply(5, 6)) # значение чисел которые будут умножаться
print(divide(10, 2)) # значение чисел которые будут делится

@Less
def scaled_add(a, b):
    return a + b

@Less
def scaled_subtract(a, b):
    return a - b

@Less
def scaled_multiply(a, b):
    return a * b

@Less
def scaled_divide(a, b):
    return a / b

print("Коэфицент 2.1 в меньшую сторону")
print(scaled_add(3, 4))
print(scaled_subtract(8, 3))
print(scaled_multiply(5, 6))
print(scaled_divide(10, 2))