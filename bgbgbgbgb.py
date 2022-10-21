numero0=int(input("Введіть число: "))
numero1=int(input("Введіть початок діапазону: "))
numero2=int(input("Введіть кінець діапазону: "))
for j in range(numero1, numero2):
    print(f"{numero0} * {j}={numero0 * j}")
    j=+1