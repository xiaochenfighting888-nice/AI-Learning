class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ", " + repr(self.rest)
        else:
            rest_repr = ""
        return "Link(" + repr(self.first) + rest_repr + ")"

    def __str__(self):
        string = "<"
        while self.rest is not Link.empty:
            string += str(self.first) + " "
            self = self.rest
        return string + str(self.first) + ">"


def square(x):
    return x * x


def odd(x):
    return x % 2 == 1


def range_link(start, end):
    """
    返回一个链表 Link，包含从 start 到 end-1 的连续整数

    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))


def map_link(f, s):
    """
    返回一个新链表 Link，其中每个元素是原链表 s 中对应元素 x 经过函数 f(x) 映射后的结果

    >>> map_link(square, range_link(3, 6))
    Link(9, Link(16, Link(25)))
    """
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))


def filter_link(f, s):
    """
    返回一个新链表 Link，仅包含原链表 s 中满足函数 f(x) 为真的元素

    >>> filter_link(odd, range_link(3, 6))
    Link(3, Link(5))
    """
    if s is Link.empty:
        return s

    filtered_rest = filter_link(f, s.rest)

    if f(s.first):
        return Link(s.first, filtered_rest)
    else:
        return filtered_rest
