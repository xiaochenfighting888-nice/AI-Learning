# 按个位数对序列 s 中的整数进行分组，并返回对应字典
# 字典的键是个位数字，值是个位数等于该键的元素列表
def digit_dict1(s):
    """
    >>> digit_dict1([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    # 自己写
    dicts = {}
    for i in s:
        x = i % 10
        if x in dicts:
            dicts[x].append(i)
        else:
            dicts[x] = [i]
    return dict(sorted(dicts.items()))


def digit_dict2(s):
    """
    >>> digit_dict2([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    return {
        d: [i for i in s if i % 10 == d]
        for d in range(10)
        if any([i % 10 == d for i in s])
    }
