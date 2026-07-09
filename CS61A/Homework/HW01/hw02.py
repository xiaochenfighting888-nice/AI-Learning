from operator import pow


def two_of_three(i, j, k):
    """接收三个正数作为参数，返回其中两个最小数的平方和。函数体只能用一行代码完成

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    return pow(i, 2) + pow(j, 2) + pow(k, 2) - pow(max(i, j, k), 2)
