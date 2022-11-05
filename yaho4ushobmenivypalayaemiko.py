#ls = [4, 2, 6, 8, 1, 9, 12]
#for i in ls:
    #print(i, end='')

#print()

#for i in range(len(ls)):
    #print(ls[i], end=' ')

# print(*ls)

#for i in range(2, 4):
    #print(ls[i])
#ls[start:end:step]
#print(type(ls[2:5]))
#print(ls[2::2])
ls = ['Milk', 'Water', 'Coffee']
print(*ls)
ls.append("Bread")
print(*ls)
ls.sort()
test = ['Apple', 'Banana']
ls.extend(test)
ls.reverse()
print(*ls)