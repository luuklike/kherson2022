string = str(input("Введіть текст: "))
exist = str(string.lower())
part1, part2 = exist.split('description')
print("description:", part2)