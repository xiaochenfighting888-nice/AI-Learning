def a_plus_abs_b(a, b):
    """返回 a + |b| 的值，禁止使用 abs 函数

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:

        def f(a, b):
            return a - b

    else:

        def f(a, b):
            return a + b

    return f(a, b)
