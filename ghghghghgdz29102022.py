while True:
    try:
        string = str(input("Введіть текст: "))
        exist = str(string.lower())
        part1, part2 = exist.split('description')
        print("description:", part2)
        break
    except:
        print("Будь ласка, напишіть descrition перед початком опису")