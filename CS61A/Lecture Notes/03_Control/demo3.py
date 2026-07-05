'''
利用命令行python -m doctest demo2.py执行
    doctest会扫描demo2.py文件，找到写在文档字符串（"""..."""）里的Python交互示例，然后：
        1.把例子当成真的代码执行
        2.对比实际输出​和写的输出
        3.不一样就报错

利用命令行python -m doctest -v demo3.py执行
    自动执行demo3.py中所有文档字符串里的>>>示例，并报告哪些通过、哪些失败
'''


def divide_exact(n, d):
    """
    返回n除以d的商和余数的函数

    >>> quotient, remainder = divide_exact(2026, 10)
    >>> quotient
    202
    >>> remainder
    6
    """
    return n // d, n % d
