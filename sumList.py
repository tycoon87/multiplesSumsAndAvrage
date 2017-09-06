a = [1, 2, 5, 10, 255, 3]
x = 0
for i in range(len(a)):
    if i < len(a):
        x = x+a[i]
print(x)