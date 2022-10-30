#
# Merge sort Сортировка слиянием
#


def merge_list(a, b):
    c = []
    x = len(a)
    y = len(b)

    i = 0
    j = 0

    while i < x and j < y:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return c


def split_arrays(array_):
    middle = len(array_) // 2
    left = array_[:middle]
    right = array_[middle:]

    if len(left) > 1:
        left = split_arrays(left)
    if len(right) > 1:
        right = split_arrays(right)

    return merge_list(left, right)


a = [1, 3, 8, 5, 3, 9, 2]
a = split_arrays(a)

print(a)
