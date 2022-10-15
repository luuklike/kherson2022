import math as pashalox
print("Програма для обчислення дискримінанта b*b - 4 * a * c")
while True:
    try:
        a = int(input("Введіть значення a: "))
        b = int(input("Введіть значення b: "))
        c = int(input("Введіть значення c: "))
        D = b*b - 4 * a * c
        if a == 0:
            print("Неправильне значення змінної а")
        if b == 0:
            print("Неправильне значення змінної b")
        if c == 0:
            print("Неправильне значення змінної с")
        elif D < 0:
            print("Результат менше 0")
        elif D > 0:
            x1 = (-b + pashalox.sqrt(D))/(2*a)
            x2 = (-b - pashalox.sqrt(D))/(2*a)
            print(f"D: {D} x1 = {x1}, x2 = {x2}")
        elif D == 0:
            x = (-b)/(2/a)
            print(f"D: {D} x1 = {x1}, x2 = {x2}")
        else:
            print("Помилка")
    except:
        print("Сталася помилка. Можливо, ви ввели не число або воно дорівнює 0. Якщо хочете повідомити про баг, зверніться до розробника: t.me/ya_n_fei")