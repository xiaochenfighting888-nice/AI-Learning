# `HW01`学习记录
## 本次练习内容
- `a_plus_abs_b`：根据 b 的正负情况选择不同计算方式，返回 a + |b| 的结果
- `two_of_three`：计算三个数中最小两个数的平方和
- `largest_factor`：查找一个整数小于自身的最大因子
- `hailstone`：生成冰雹序列并返回序列长度

## 问题
~~~python
def a_plus_abs_b(a, b):
    """返回 a + |b| 的值，禁止使用 abs 函数。

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
~~~

~~~powershell
(base) PS D:\study\ai-learning\cs61a\homework\hw01> python -m doctest hw01.py
**********************************************************************
File "D:\study\ai-learning\cs61a\homework\hw01\hw01.py", line 4, in hw01.a_plus_abs_b
Failed example:
    a_plus_abs_b(2, 3)
Expected:
        5
Got:
    5
**********************************************************************
1 item had failures:
   1 of   4 in hw01.a_plus_abs_b
***Test Failed*** 1 failure.
~~~

## 解决

​	`doctest` 要求 `>>>` 和输出在同一列，多缩进了 5 ，`doctest` 会把那行空格也算进去，而 `doctest` 逐字符比较输出，因此结果会不同，然后报错。

## 知识补充

### lambda 写法

~~~python
# HW01 lambda 写法
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
    # lambda 是 Python 中用于创建匿名函数的语法，适用于定义逻辑简单、一次性使用的函数对象
    # 语法：lambda 参数列表: 表达式
    # lambda是关键字
    # 参数列表可以为空，也可以有多个参数
    # 冒号后只能是一个表达式，不能是多条语句
    # 表达式的值自动作为返回值，无需 return
    if b < 0:
        f = lambda a, b: a - b
    else:
        # lambda a, b: a + b
        # \____/ \__/  \___/
        # 关键字  参数  返回值
        f = lambda a, b: a + b
    return f(a, b)
~~~
