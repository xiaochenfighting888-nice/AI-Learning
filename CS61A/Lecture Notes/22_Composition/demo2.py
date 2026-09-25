class Tree:
    def __init__(self, label, branches=[]):
        """创建一棵以 label 为根标签、branches 为子树的树"""
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        """返回树的 Python 表示形式"""
        if self.branches:
            branch_str = ", " + repr(self.branches)
        else:
            branch_str = ""
        return "Tree({0}{1})".format(repr(self.label), branch_str)

    def __str__(self):
        """返回树的缩进字符串表示"""
        return "\n".join(self.indented())

    def indented(self):
        """返回按树层级缩进后的字符串列表"""
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append("  " + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        """判断当前树是否为叶子节点"""
        return not self.branches


def fib_tree(n):
    """返回表示第 n 个斐波那契数递归计算过程的树"""
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])


def leaves(t):
    """返回树 t 中所有叶子节点标签组成的列表"""
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for b in t.branches:
            all_leaves.extend(leaves(b))
        return all_leaves


def height(t):
    """返回树 t 的高度，叶子节点的高度为 0"""
    if t.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in t.branches])


def prune(t, n):
    """删除树 t 中所有根标签为 n 的分支"""
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)
