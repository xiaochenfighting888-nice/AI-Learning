# 判断序列 s 中的每个元素是否都至少存在另一个与它相等的元素
def all_have_an_equal1(s):
    """
    >>> all_have_an_equal1([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal1([4, 3, 2, 3, 2, 4])
    True
    """
    # 自己写
    dicts = {d: [x for x in s if x == d] for d in s}
    for i in dicts.values():
        if len(i) <= 1:
            return False
    return True


def all_have_an_equal2(s):
    """
    >>> all_have_an_equal2([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal2([4, 3, 2, 3, 2, 4])
    True
    """
    return all([s[i] in s[:i] + s[i + 1 :] for i in range(len(s))])


def all_have_an_equal3(s):
    """
    >>> all_have_an_equal3([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal3([4, 3, 2, 3, 2, 4])
    True
    """
    return all([sum([1 for y in s if y == x]) > 1 for x in s])


def all_have_an_equal4(s):
    """
    >>> all_have_an_equal4([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal4([4, 3, 2, 3, 2, 4])
    True
    """
    return min([sum([1 for y in s if y == x]) for x in s]) > 1


def all_have_an_equal5(s):
    """
    >>> all_have_an_equal5([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal5([4, 3, 2, 3, 2, 4])
    True
    """
    return min([s.count(x) for x in s]) > 1
