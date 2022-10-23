line = input("Enter line: ").lower().replace(' ', '')
print(line, line[::-1])
print(line == line[::-1])