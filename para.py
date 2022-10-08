n = int(input("Enter number from range 0-10 but not 5: "))
try:
    if n == 5:
        raise ValueError("You wrote 5 its bad")
except ValueError as e:
    print(str(e))
