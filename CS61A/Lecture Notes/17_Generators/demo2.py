def count_partitions_basic(n, m):
    """返回将 n 划分为不超过 m 的正整数之和的方案数"""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions_basic(n - m, m)
        without_m = count_partitions_basic(n, m - 1)
        return with_m + without_m


def count_partitions_exact_match(n, m):
    """使用 exact_match 思路计算 n 的整数划分方案数"""
    if n < 0 or m == 0:
        return 0
    else:
        exact_match = 0
        if n == m:
            exact_match = 1
        with_m = count_partitions_exact_match(n - m, m)
        without_m = count_partitions_exact_match(n, m - 1)
        return exact_match + with_m + without_m


def list_partitions(n, m):
    """返回 n 的所有整数划分，每个划分使用列表表示"""
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [[m]]
        with_m = [p + [m] for p in list_partitions(n - m, m)]
        without_m = list_partitions(n, m - 1)
        return exact_match + with_m + without_m


def partitions(n, m):
    """依次产生 n 的所有整数划分的字符串表示"""
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partitions(n - m, m):
            yield p + "+" + str(m)
        yield from partitions(n, m - 1)
