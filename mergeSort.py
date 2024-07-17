# Merge Sort

def mergeSort(a):
    if len(a) <=1:
        return a
    mid = len(a)//2
    l = a[:mid]
    r = a[mid:]
    return merge(mergeSort(l),mergeSort(r))


def merge(l,r):
    result=[]
    i,j=0,0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i+=1
        else:            
            result.append(r[j])
            j+=1
    result += l[i:]
    result += r[j:]
    return result

a = [2,8,5,3,9,4,1]
print(mergeSort(a))
