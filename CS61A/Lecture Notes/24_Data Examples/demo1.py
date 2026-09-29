# 返回序列 s 中绝对值最小的元素所对应的所有索引
def min_abs_indices1(s):
    """
    >>> min_abs_indices1([-4, -3, -2, 3, 2, 4])
    [2, 4]
    >>> min_abs_indices1([1, 2, 3, 4, 5])
    [0]
    """
    # 自己编写
    min_abs = min([abs(b) for b in s])
    j = 0
    indices = []
    for i in s:
        if i >= 0:
            if i == min_abs:
                indices.append(j)
        else:
            if -i == min_abs:
                indices.append(j)
        j += 1
    return indices


def min_abs_indices2(s):
    """
    >>> min_abs_indices2([-4, -3, -2, 3, 2, 4])
    [2, 4]
    >>> min_abs_indices2([1, 2, 3, 4, 5])
    [0]
    """
    min_abs = min(map(abs, s))
    return [i for i in range(len(s)) if abs(s[i]) == min_abs]
