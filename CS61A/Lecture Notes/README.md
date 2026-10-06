# CS61A Lecture Notes 文件索引

每一章列出实际存在的文件及其主要用途：`notes.md` 是知识笔记，`demo*.py` 是对应主题的代码示例。

## 课程路线

| 课程部分 | 章节 | 复习主线 |
| --- | --- | --- |
| Python 与函数 | 01–10 | 表达式、函数、控制流程、环境图、高阶函数、递归 |
| 数据结构 | 11–17 | 序列、容器、数据抽象、树、可变性、迭代器、生成器 |
| 面向对象与效率 | 18–24 | 对象、属性、继承、表示、链表与树、复杂度、数据练习 |
| Scheme 与解释器 | 25–30 | Scheme、解释器、尾调用、代码即数据、宏 |
| SQL 与数据库 | 31–34 | 查询、连接、聚合、表更新 |
| 综合练习 | 35 | 将递归、树结构和程序设计步骤用于综合问题 |

## Python 与函数

### 01 Expressions｜表达式

| 文件 | 内容 |
| --- | --- |
| notes.md | 中缀表达式、函数调用表达式和表达式树。 |
| demo.py | 对比运算符表达式与 `add` / `mul` 调用，演示嵌套表达式的求值。 |

### 02 Functions｜函数

| 文件 | 内容 |
| --- | --- |
| notes.md | 内置函数、赋值、环境图、函数定义，以及 `print` 和 `None`。 |
| demo.py | 名称赋值、圆面积与周长、自定义平方函数，以及 `print` 的返回值。 |

### 03 Control｜控制流程

| 文件 | 内容 |
| --- | --- |
| notes.md | 多重环境、文档字符串、Doctest、复合语句、条件与循环。 |
| demo1.py | 算术运算、`operator` 模块、商和余数，以及多返回值解包。 |
| demo2.py | `divide_exact` 示例，配合 `python -i` 在交互环境中检查变量。 |
| demo3.py | 为 `divide_exact` 写 Doctest，可用 `python -m doctest -v demo3.py` 执行。 |

### 04 Higher-Order Functions｜高阶函数

| 文件 | 内容 |
| --- | --- |
| notes.md | 迭代、斐波那契、`and` / `or` 短路求值和高阶函数。 |
| demo1_fibonacci.py | 用递归计算斐波那契数列。 |
| demo2_evaluation_order.py | 对比 `if` 与普通函数调用的参数求值顺序；运行到 `sqrt(-16)` 时会产生预期的错误。 |
| demo3_short_circuit.py | 用短路求值避免对负数开方或执行不必要的表达式。 |
| demo4_area_abstraction.py | 将不同图形的面积公式抽象为共用计算过程。 |
| demo5_higher_order_functions.py | 用 `summation` 复用求和逻辑，计算自然数和、立方和与圆周率近似。 |

### 05 Environments｜环境与柯里化

| 文件 | 内容 |
| --- | --- |
| notes.md | 高阶函数和嵌套函数的环境图、局部名称、函数组合、`lambda` 与柯里化。 |
| demo1.py | 对比用 `lambda` 和 `def` 定义平方函数。 |
| demo2.py | 实现 `curry`，把双参数函数改成连续单参数调用。 |

### 06 Sounds｜声音

| 文件 | 内容 |
| --- | --- |
| notes.md | WAV 文件与用 Python 生成声音的基本方法。 |
| demo.py | 生成波形、组合音符与旋律，并将采样写成 `song.wav`；运行后会在当前目录创建音频文件。 |

### 07 Functional Abstraction｜函数抽象

| 文件 | 内容 |
| --- | --- |
| notes.md | 函数抽象、返回语句、名称选择、接口和用名称简化表达式。 |
| demo.py | 用 `search` 和 `inverse` 按条件搜索输入；目标不存在时搜索不会结束。 |

### 08 Function Examples｜函数示例

| 文件 | 内容 |
| --- | --- |
| notes.md | 装饰器及其等价写法，用包装函数跟踪调用。 |
| demo1.py | 从整数中删除指定数字，并逐位重建结果。 |
| demo2.py | 用 `trace1` 装饰平方和函数，在调用前打印跟踪信息。 |

### 09 Recursion｜递归

| 文件 | 内容 |
| --- | --- |
| notes.md | 闭包、递归函数、调用环境，以及递归和迭代之间的转换。 |
| demo.py | 递归求数字和与 Luhn 校验和，演示两个辅助函数交替调用。 |

### 10 Tree Recursion｜树形递归

| 文件 | 内容 |
| --- | --- |
| notes.md | `cascade`、`inverse_cascade`、树形递归斐波那契和整数划分；本章代码示例写在笔记中，没有独立 `.py` 文件。 |

## 数据结构与迭代

### 11 Sequences｜序列

| 文件 | 内容 |
| --- | --- |
| notes.md | 列表、索引、遍历、解包、`range` 和列表推导式。 |
| demo.py | 用列表推导式查找一个数的所有正因数。 |

### 12 Containers｜容器

| 文件 | 内容 |
| --- | --- |
| notes.md | 嵌套数据、方框指针图、切片与浅拷贝、聚合函数、字符串和字典。 |
| demo.py | 组合字典与列表推导式，根据匹配条件为多个键收集对应的值。 |

### 13 Data Abstraction｜数据抽象

| 文件 | 内容 |
| --- | --- |
| notes.md | 抽象屏障、抽象数据类型、构造器与选择器，并以有理数运算为例。 |
| demo.py | 用闭包表示有理数，提供取分子、取分母、加法、乘法和相等判断。 |

### 14 Trees｜树

| 文件 | 内容 |
| --- | --- |
| notes.md | 树的节点、根标签、分支、叶子和递归定义。 |
| demo.py | 用列表表示树，递归实现遍历、路径和、叶子处理与路径计数。 |

### 15 Mutability｜可变性

| 文件 | 内容 |
| --- | --- |
| notes.md | 对象、可变与不可变对象、别名、对象身份、元组与字符串编码。 |
| demo.py | 用闭包和可变列表保存余额，实现有状态的取款函数。 |

### 16 Iterators｜迭代器

| 文件 | 内容 |
| --- | --- |
| notes.md | 可迭代对象与迭代器、`next`、迭代耗尽、字典遍历，以及 `map`、`filter`、`zip` 等操作。 |
| demo.py | 用 `zip`、`reversed` 和 `all` 判断序列是否为回文。 |

### 17 Generators｜生成器

| 文件 | 内容 |
| --- | --- |
| notes.md | `yield`、生成器的暂停与恢复、结束方式和 `yield from`。 |
| demo1.py | 生成倒计时、字符串前缀和子串。 |
| demo2.py | 用递归计数、列举和惰性生成整数划分方案。 |

## 面向对象与数据示例

### 18 Objects｜对象

| 文件 | 内容 |
| --- | --- |
| notes.md | 面向对象编程、类、实例、属性、方法、`self` 和对象身份；没有独立 `.py` 演示文件。 |

### 19 Attributes｜属性

| 文件 | 内容 |
| --- | --- |
| notes.md | `class` 语句、实例属性和类属性、属性查找、绑定方法及方法对象。 |
| demo.py | 用 `Account` 展示实例属性、类属性以及给单个实例设置属性。 |

### 20 Inheritance｜继承

| 文件 | 内容 |
| --- | --- |
| notes.md | 方法继承和重写、属性查找顺序、继承与组合，以及多继承。 |
| demo.py | 通过银行账户子类演示手续费、方法重写、多继承和银行统一管理账户。 |

### 21 Representation｜对象表示

| 文件 | 内容 |
| --- | --- |
| notes.md | `repr` / `str`、字符串插值、特殊方法、运算符行为和接口。 |
| demo.py | 定义 `Ratio` 有理数类，演示 `__repr__`、`__str__`、加法和浮点转换。 |

### 22 Composition｜组合数据结构

| 文件 | 内容 |
| --- | --- |
| notes.md | `Link` 链表、树类，以及用函数表示树。 |
| demo1.py | 实现链表节点、区间链表、映射和筛选。 |
| demo2.py | 实现树类、斐波那契树、叶子收集、高度计算和剪枝。 |

### 23 Efficiency｜效率

| 文件 | 内容 |
| --- | --- |
| notes.md | 记忆化、快速幂、增长阶、运行时间与空间消耗。 |
| demo1.py | 用函数包装器统计调用次数，并比较 Fibonacci 加入记忆化前后的重复计算。 |
| demo2.py | 统计递归中同时存在的调用数，用于观察调用栈空间。 |

### 24 Data Examples｜数据结构练习

| 文件 | 内容 |
| --- | --- |
| notes.md | 列表对象、别名、`append` / `extend`、复制、切片赋值与循环引用。 |
| demo1.py | 找出绝对值最小的元素及其所有索引。 |
| demo2.py | 用相邻元素对计算最大相邻和。 |
| demo3.py | 按整数的个位数分组并构造字典。 |
| demo4.py | 多种写法判断序列中每个元素是否至少重复出现一次。 |
| demo5.py | 在链表上检查排序并合并有序链表，比较新建节点和原地修改。 |

## Scheme 与程序语言

### 25 Scheme

| 文件 | 内容 |
| --- | --- |
| notes.md | Scheme 基本表达式、过程定义、`lambda`、`cond`、`begin` 和 `let`。 |

### 26 Scheme List｜Scheme 列表

| 文件 | 内容 |
| --- | --- |
| notes.md | `cons`、`car`、`cdr`、`nil`、递归列表、符号、`quote` 和列表内置过程。 |

### 27 Interpreters｜解释器

| 文件 | 内容 |
| --- | --- |
| notes.md | Python 异常、编程语言的编译与解释，以及 Scheme 表达式的读取、词法分析和语法分析。 |

### 28 Tail Calls｜尾调用

| 文件 | 内容 |
| --- | --- |
| notes.md | 函数式编程、递归空间、尾位置与尾递归，以及用 `reduce` / `map` 构造列表。 |

### 29 Programs as Data｜代码即数据

| 文件 | 内容 |
| --- | --- |
| notes.md | `eval`、生成 Scheme 表达式、`quote`、准引用和用程序生成程序。 |

### 30 Macros｜宏

| 文件 | 内容 |
| --- | --- |
| notes.md | Scheme 宏、`define-macro`、准引用，以及在 Python 和 Scheme 中跟踪递归调用。 |

## SQL 与数据库

### 31 SQL

| 文件 | 内容 |
| --- | --- |
| notes.md | `SELECT`、结果表、列名、集合查询、建表与基本查询结构。 |

### 32 Tables｜多表查询

| 文件 | 内容 |
| --- | --- |
| notes.md | 笛卡尔积、`JOIN`、多表查询、表别名，以及 SQL 数值、比较、逻辑和字符串表达式。 |

### 33 Aggregation｜聚合

| 文件 | 内容 |
| --- | --- |
| notes.md | `max` / `min`、`avg` / `count`、`DISTINCT`、`GROUP BY`、`HAVING` 与聚合查询顺序。 |

### 34 Databases｜数据库操作

| 文件 | 内容 |
| --- | --- |
| notes.md | 建表约束、插入数据、更新和删除行，以及删除表。 |

## 综合复习

### 35 Final Examples

| 文件 | 内容 |
| --- | --- |
| notes.md | 用递归处理树上的祖先比较与后代比较，并整理数据定义、类型签名和测试等设计步骤。 |
