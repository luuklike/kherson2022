import math as pashalox
print("Програма для обчислення дискримінанта b*b - 4 * a * c")
while True:
    try:
        a = int(input("Введіть значення a: "))
        b = int(input("Введіть значення b: "))
        c = int(input("Введіть значення c: "))
        D = b*b - 4 * a * c
        if a == -0:
            print("Ти шо, тютю? Яке -0? Постав нормальну змінну а")
        if b == -0:
            print("Ти шо, тютю? Яке -0? Постав нормальну змінну b")
        if c == -0:
            print("Ти шо, тютю? Яке -0? Постав нормальну змінну с")
        elif D < 0:
            print("Помилка. Результат менше 0")
        elif D > 0:
            x1 = (-b + pashalox.sqrt(D))/(2*a)
            x2 = (-b - pashalox.sqrt(D))/(2*a)
            print(f"D: {D} x1 = {x1}, x2 = {x2}")
            break
        elif D == 0:
            x = (-b)/(2/a)
            print(f"D: {D} x1 = {x1}, x2 = {x2}")
        else:
            print("Помилка")
    except:
        print("Сталася помилка. Можливо, ви ввели не число. Якщо хочете повідомити про баг, зверніться до розробника: t.me/ya_n_fei")