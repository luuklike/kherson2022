import math as pashalox
print("Обчислити дискримінацію")
try:
    a = int(input("Введіть змінну a: "))
    b = int(input("Введіть змінну b: "))
    c = int(input("Введіть змінну c: "))
    D = b*b - 4 * a * c

    if D > 0:
        x1 = (-b + pashalox.sqrt(D))/(2*a)
        x2 = (-b - pashalox.sqrt(D))/(2*a)
        print(f"D: {D} x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x = (-b)/(2/a)
        print(f"D: {D} x1 = {x1}, x2 = {x2}")
    elif D < 0:
        print("Число має бути більше 1")
    else:
        print("Число має бути більше 1")
except:
    print("Сталася помилка. Можливо, ви ввели не число. Якщо це помилка програми, зверніться до розробника: t.me/ya_n_fei")