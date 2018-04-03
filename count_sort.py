def sort_count(l,a,b):
    l_counter = [0]*(b-a+1)

    for i in l:
        l_counter[i-a] += 1

    sorted_l = [0]*len(l)
    start_index = 0
    for freq_index in range(len(l_counter)):
        for j in range(l_counter[freq_index]):
            sorted_l[start_index] = freq_index +a
            start_index +=1
    return sorted_l



if __name__=='__main__':
    print(sort_count([-1,2,3,2,1,2,4,4,4,3,1],-1,4))