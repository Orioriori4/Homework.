def addition(a, b):
    return a + b
def subtraction(a, b):
    return  a - b
def Multiplication(a, b):
    return a * b
def Division(a, b):
    if b == 0:
        return print("Делить на 0 нельзя")
    else:
        return a / b

print("Что ты хочешь сделать:")
print("1Сложить,"
      "2Вычесть,"
      "3Умножить,"
      "4Разделить")
option = input()
chislo1 = float(input("Введите первое число"))
chislo2 = float(input("Введите второе число"))
if option == "1":
    print(f"{chislo1}+{chislo2}={addition(chislo1, chislo2)}")
elif option == "2":
    print(f"{chislo1}-{chislo2}={subtraction(chislo1, chislo2)}")
elif option == "3":
    print(f"{chislo1}*{chislo2}={Multiplication(chislo1, chislo2)}")
elif option == "4":
    print(f"{chislo1}/{chislo2}={Division(chislo1, chislo2)}")
else:
    print("Ты ввел что-то не то")