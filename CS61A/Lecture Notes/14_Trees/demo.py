def tree(label, branches=[]):
    """构造一棵以 label 为根标签、branches 为分支的树"""
    for branch in branches:
        assert is_tree(branch), "branches must be trees"
    return [label] + list(branches)


def label(tree):
    """返回树的根标签"""
    return tree[0]


def branches(tree):
    """返回树的分支"""
    return tree[1:]


def is_leaf(tree):
    """判断是否是叶子节点"""
    return not branches(tree)


def is_tree(tree):
    """判断是否为一棵合法树"""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def fib_tree(n):
    """返回表示第 n 个斐波那契数计算过程的树"""
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        return tree(label(left) + label(right), [left, right])


def count_leaf(tree):
    """返回树中叶子节点的个数"""
    if is_leaf(tree):
        return 1
    else:
        return sum([count_leaf(branch) for branch in branches(tree)])


def leaves(tree):
    """返回所有叶子节点标签组成的列表"""
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(branch) for branch in branches(tree)], [])


def increment_leaves(t):
    """返回一棵新树，将所有叶子节点的标签加 1"""
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(branch) for branch in branches(t)]
        return tree(label(t), bs)


def increment(t):
    """返回一棵新树，将所有节点的标签加 1"""
    return tree(label(t) + 1, [increment(branch) for branch in branches(t)])


def print_sums(tree, so_far):
    """打印从根节点到每个叶子节点路径上的标签之和"""
    so_far = so_far + label(tree)
    if is_leaf(tree):
        print(so_far)
    else:
        for branch in branches(tree):
            print_sums(branch, so_far)


def count_paths(t, total):
    """返回树中从当前节点向下、标签之和等于 total 的路径数量"""
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum(
        [count_paths(branch, total - label(t)) for branch in branches(t)]
    )


if __name__ == "__main__":
    print(tree(1))
    t = tree(3, [tree(1, [tree(7)]), tree(6)])
    print(t)
    print(label(t))
    print(branches(t))
    print(fib_tree(4))
    print(count_leaf(t))
    print(increment_leaves(t))
    print(increment(t))
    print(leaves(t))
    print_sums(t, 0)
    print(count_paths(t, 3))
