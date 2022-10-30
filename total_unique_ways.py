from datetime import datetime


#                        1      2     3    4
#                     -------------------------
#                4    |     |     |     |     |
#                     -------------------------
#                3    |     |     |     |  D  |
#                     -------------------------
#                2    |     |     |     |     |
#                     -------------------------
#                1    |  R   |     |     |    |
#                     -------------------------

# Robot can move only up and right and always in 1 , 1 coordinates
# In our case  he must go in 3, 4
# Our problem find all unique ways

def ways(n: int, m: int):
    if n < 1 or m < 1:
        return 0
    if n == 1 and m == 1:
        return 1
    else:
        return ways(n - 1, m) + ways(n, m - 1)


# print(ways(4, 5))   # Time for work 2**m*n


# now the best way  # time m*n

def ways_1(n, m):
    p = [[0] * (m + 1) for _ in range(n + 1)]
    return helper(n, m, p)


def helper(n, m, array: list):
    if n < 1 or m < 1:
        return 0
    if n == 1 and m == 1:
        return 1
    if array[n][m] != 0:
        return array[n][m]
    array[n][m] = helper(n - 1, m, array) + helper(n, m - 1, array)
    return array[n][m]


# time_1 = datetime.now().second
# print(ways(15, 15))
# time_1_1 = datetime.now().second
# print(time_1_1 - time_1)

time_2 = datetime.now().second
print(ways_1(150, 150))
time_2_1 = datetime.now().second
print(time_2_1 - time_2)
