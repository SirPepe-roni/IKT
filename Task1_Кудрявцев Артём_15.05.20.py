print("Введите число: ")
n=int(input())
a = []
for i in range(n + 1):
    a.append(i)   
i = 2
while i <= n:
    if a[i] != 0:
        j = i + i
        while j <= n:
           a[j] = 0
           j = j + i
    i += 1
a = set(a)
a.remove(0)
if n in a:
    print("Простое")
else:
    print("Сложное")
