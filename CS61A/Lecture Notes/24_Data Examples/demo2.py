# 返回序列 s 中所有相邻元素对的最大和
def largest_adj_sum1(s):
    """
    >>> largest_adj_sum1([-4, -3, -2, 3, 2, 4])
    6
    >>> largest_adj_sum1([-4, 3, -2, -3, 2, -4])
    1
    """
    # 自己写
    return max([(s[x] + s[x + 1]) for x in range(len(s) - 1)])


def largest_adj_sum2(s):
    """
    >>> largest_adj_sum2([-4, -3, -2, 3, 2, 4])
    6
    >>> largest_adj_sum2([-4, 3, -2, -3, 2, -4])
    1
    """
    return max([a + b for a, b in zip(s[:-1], s[1:])])
