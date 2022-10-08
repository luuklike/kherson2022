n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 > n2 and n2 > n3:
    print("Max number is, ", n1)
elif n1 < n2 and n2 > n3:
    print("Max number is, ", n2)
elif n1 == n2 and n2 == n3:
    print("Вони однакові")
else:
    print("Max number is, ", n3)