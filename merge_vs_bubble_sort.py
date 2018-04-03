
#### comparison between merge sort and bubble sort ###

import numpy as np
import time
import merge_sort as ms
import bubble_sort as bs
import random
random.seed(100)


def test(l1,algorithm_no = 1):
    start = time.time()

    if algorithm_no == 1:
        ms.merge_sort(l1)
    elif algorithm_no == 2:
        bs.bub_sort(l1)

    end = time.time()
    return (end-start)

def compare_algorithms(sample=6000):
    l1 = np.random.normal(size=sample)
    l2 = list(l1)

    merge_result = test(l1, algorithm_no=1)
    bubble_result = test(l2, algorithm_no=2)

    return  'Merge sort takes {0} sec. less ' \
            'than bubble sort (for sample of {1} elements list)'.format(merge_result - bubble_result,sample)

if __name__=='__main__':
    print(compare_algorithms())


