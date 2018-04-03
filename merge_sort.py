#!home/kodolamacz/anaconda3/bin/python3.6

def merge(L,R,Arr):
    i,j,k = 0,0,0
    nl = len(L)
    nr = len(R)
    na = len(Arr)

    while i<na and j<nl and k< nr:

        if L[j] <= R[k]:
            Arr[i] = L[j]
            i,j = i + 1, j + 1
        else:
            Arr[i] = R[k]
            i,k = i + 1, k + 1

    while i<na and j<nl :
        Arr[i] = L[j]
        i,j = i + 1, j + 1

    while i<na and k<nr:
        Arr[i] = R[k]
        i,k = i + 1, k + 1

    return Arr


def merge_sort(Arr):
    if len(Arr) == 1:
        return Arr      #recurrsion ends when Array consists of 1 element - it is 1 sorted element
    else:
        na = len(Arr)
        mid = na//2
        L=[]
        R=[]

        L = Arr[:mid]
        R = Arr[mid:]

        merge_sort(L)   #recursive formula
        merge_sort(R)   #recursive formula

        return merge(L,R,Arr)


if __name__=='__main__':

    l1=[1,4,3,10,2,5,0,7]
    print(merge_sort(l1))
