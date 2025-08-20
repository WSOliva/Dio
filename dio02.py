numeros = [2, 5, 65, 3, 43, 8, 66, 22, 12, 54, 33, 90, 67, 45, 2, 2]
for i in numeros:
    if i % 2 == 0:
        print(i, end=' ')
num = [5, 2, 8, 0]
numeros.extend(num)
print(numeros)
print(numeros.index(2))
for i in numeros:
    if i == 2:
        numeros.remove(2)
print(numeros)
