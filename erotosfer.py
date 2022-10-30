# Algorithm to find simple numbers in 0 - 10000

lenght = 10000


def is_simple(x: int):

    a = [True] * lenght
    a[0] = a[1] = False

    for i in range(2, int(lenght**0.5)+1):
        if a[i]:
            for j in range(2*i, lenght, i):
                a[j] = False
    return a[x]


# test
print(is_simple(239))
