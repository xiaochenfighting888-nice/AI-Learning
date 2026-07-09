def largest_factor(n):
    """接收一个大于 1 的整数 n，返回小于 n 且能被 n 整除的最大整数

    >>> largest_factor(15) # 因子是 1, 3, 5
    5
    >>> largest_factor(80) # 因子是 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # 因子只有 1，因为 13 是质数
    1
    """
    max_num = 1
    for i in range(1, n):
        if n % i == 0:
            max_num = i
    return max_num
