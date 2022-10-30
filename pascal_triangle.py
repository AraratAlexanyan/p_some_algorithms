#       1                            1 0 0 0 0
#      1  1                          1 1 0 0 0
#    1   2  1        example         1 2 1 0 0
#   1  3   3  1                      1 3 3 1 0
#  1  4  6   4  1                    1 4 6 4 1

def make_triangle(n: int):
    triangle = []
    for _ in range(n+1):
        triangle.append([1]+[0]*n)
    for i in range(1, n+1):
        for j in range(1, i+1):
            triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]

    for i in range(0, n+1):
        for j in range(0, i+1):
            print(triangle[i][j],  end=' ')
        print()


make_triangle(15)
