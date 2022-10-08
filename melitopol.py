from wsgiref.simple_server import WSGIRequestHandler


n = int(input("Раз: "))
i = int(input("Друге: "))
for d in range(n, i):
    if d % 7 == 0:
        print(d)