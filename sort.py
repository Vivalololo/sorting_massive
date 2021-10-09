import random
a = []
n = int(input('введите колво чисел '))
for i in range (n):
    x = random.randint(-999, 999)
    a.append(x)
print(a)

for u in range (0, n-1):
    for i in range (n-1, u, -1):
        if a[i] < a[i-1]:
            #print(i, a[i], a[i-1])
            b = a[i-1]
            a[i-1] = a[i]
            a[i] = b

print(a)