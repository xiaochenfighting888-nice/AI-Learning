def palindrome(s):
    """
    判断序列 s 是否为回文
    回文表示：从左向右读取和从右向左读取结果相同

    >>> palindrome([3,1,4,1,5])
    False
    >>> palindrome([3,1,4,1,3])
    True
    >>> palindrome('seveneves')
    True
    >>> palindrome('seven eves')
    False
    """
    # 方法一
    # return list(s) == list(reversed(s))

    # 方法二
    return all([x == y for x, y in zip(s, reversed(s))])
