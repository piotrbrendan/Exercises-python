
def ins_sort(l):

    for i in range(1,len(l)):
        pos = i
        value = l[pos]

        while value < l[pos-1] and pos>=1:
            l[pos] = l[pos-1]
            pos -= 1
        l[pos] = value
    return l

if __name__=='__main__':

    l1=[1,4,3,10,2,5,0,7]
    print(ins_sort(l1))