#Selection Sort 


a = [2,8,5,3,9,4,1]

for i in range(len(a)):
    cm = i
    for j in range(i+1,len(a)):
        if a[j] < a[cm] :
            cm=j
    a[i],a[cm] = a[cm],a[i]
print(a)