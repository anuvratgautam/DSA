#Insertion Sort


a = [2,8,5,3,9,4,1]

for i in range(len(a)):
    j=i
    while j>0 and a[j-1] > a[j]:
        a[j],a[j-1] = a[j-1],a[j]
        j=j-1

print(a)


