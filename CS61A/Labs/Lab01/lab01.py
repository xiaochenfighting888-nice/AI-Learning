def falling(n, k):
    """“递降”阶乘，接受两个参数 n 和 k，并返回从 n 开始向下数的 k 个连续数字的乘积。当 k 为 0 时，该函数应返回 1.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """

    # k为0，函数返回1
    if k == 0:
        return 1
    # k != 0
    else:
        # 保留乘积的结果
        total = 1
        # 计算到哪个数结束
        num = n - k + 1
        # “递降阶乘”
        while n >= num:
            total = total * n
            n -= 1
        return total


def divisible_by_k(n, k):
    """接受正整数 n 和 k。它打印所有小于或等于 n 且能被 k 整除的正整数，从最小到最大。然后，它返回打印了多少个数字
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """

    # 如果 n < k，那么 1 到 n 之间没有能被 k 整除的正整数
    if n < k:
        return 0
    # 被除数 >= 除数，遍历 n ~ k 的数字
    else:
        # 符合要求的个数
        num = 0
        # i遍历k ~ n的数
        i = k
        while n >= i:
            if i % k == 0:
                print(i)
                num += 1
            i += 1
        return num


def sum_digits(y):
    """接受一个非负整数并对其数字求和

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """

    total = 0
    while y // 10 != 0:
        total += y % 10
        y = y // 10
    total = total + y
    return total


def double_eights(n):
    """输入一个数字，判断该数字中是否包含两个相邻的 8
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """

    # 数字的位数至少为2
    while n // 10 != 0:
        if n % 10 == 8:
            n //= 10
            if n % 10 == 8:
                return True
        else:
            n //= 10
    # 只有一位数，返回False
    return False
