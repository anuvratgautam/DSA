# Shell Sort

a = [2,8,5,3,9,4,1]
N = len(a)

h=1
while h < N//3:
    h = 3*h + 1

while h>= 1:
    for i in range(h,N):
        j = i
        while j >= h and a[j] < a[j-h]:
            a[j-h], a[j] = a[j], a[j-h]
            j = j - h
    h= h//3

print(a)


