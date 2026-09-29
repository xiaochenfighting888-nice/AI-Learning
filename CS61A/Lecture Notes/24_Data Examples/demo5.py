def ordered(s, key=lambda x: x):
    """
    判断链表 s 中的元素按照 key 转换后的值是否为非递减顺序

    >>> ordered(Link(1, Link(3, Link(4))))
    True
    >>> ordered(Link(1, Link(4, Link(3))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))), key=abs)
    True
    >>> ordered(Link(1, Link(4, Link(3))), key=abs)
    False
    """

    if s is Link.empty or s.rest is Link.empty:
        return True
    elif key(s.first) > key(s.rest.first):
        return False
    else:
        return ordered(s.rest, key=key)


def merge(s, t):
    """
    合并两个已经有序的链表 s 和 t，并返回合并后的有序链表
    不修改 s 和 t 中已有节点之间的连接关系

    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge(a, b)
    Link(1, Link(1, Link(4, Link(5))))
    >>> a
    Link(1, Link(5))
    >>> b
    Link(1, Link(4))
    """

    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.first, merge(s.rest, t))
    else:
        return Link(t.first, merge(s, t.rest))


def merge_in_place(s, t):
    """
    原地合并两个已经有序的链表 s 和 t，并返回合并后的有序链表
    合并过程中会重新连接原链表中的节点，因此可能同时改变 s 和 t

    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge_in_place(a, b)
    Link(1, Link(1, Link(4, Link(5))))
    >>> a
    Link(1, Link(1, Link(4, Link(5))))
    >>> b
    Link(1, Link(4, Link(5)))
    """

    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        s.rest = merge_in_place(s.rest, t)
        return s
    else:
        t.rest = merge_in_place(s, t.rest)
        return t


class Link:
    """
    表示一个递归链表，每个节点包含 first 和指向剩余链表的 rest

    >>> Link(1, Link(2, Link(3)))
    Link(1, Link(2, Link(3)))
    >>> s = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> s
    Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(s)
    <1 <2 3> 4>
    """

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
