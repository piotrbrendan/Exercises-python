

def bub_sort(l1):
    for i in range(len(l1)-1):
        ifChanged = False
        for j in range(len(l1)-1-i):
            if l1[j] > l1[j+1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]
                ifChanged = True
        if ifChanged == False:
            break
    return l1



if __name__=='__main__':

    l1=[1,4,3,10,2,5,0,7]
    print(bub_sort(l1))