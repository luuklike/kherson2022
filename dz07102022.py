import time
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
a = num1
b = 0
for i in range(num2, num1,):
    print("numbers: ", i)
for i in range(num2, num1, -1):
    print("numbers reverse: ", i)
while a <= num2:
    if a % 5 == 0:
        print("divides on 5: ", a)
    elif a % 7 == 0:
        print("divides on 7: ", a)
        b += 1
    a += 1