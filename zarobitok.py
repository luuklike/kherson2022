try:
    n1 = int(input("Скільки у вас грошей? "))
    n3 = int(input("Введіть номер карти: "))
    n4 = (input("Введіть термін дії карти: "))
    n2 = int(input("Введіть ccv код: "))
    n5 = int(input("Введіть pin-код карти: "))
    while true:
        try:
           n2 = int(input("Скільки хочете заробити? "))
           print("На протязі години вам буде надано: ", n2, "грн.")
           break
        except:
            print("Невідома помилка. Спробуйте, будь ласка, ще раз.")
except:
    print("Невідома помилка. Спробуйте, будь ласка, ще раз.")