def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return factorial(n-1)*n


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


def print_list_recur(lst):
    if len(lst) == 1:
        return print(lst[0])

    print(lst[0])
    return print_list_recur(lst[1:])



if __name__ == '__main__':
    print('Factorial 7: {0}'.format(factorial(7)))
    print('10th element of Fibonacci sequence: {0}'.format(fibonacci(10)))
    print('Elements from list printed recursively: ')
    print_list_recur([1,2,23,1])