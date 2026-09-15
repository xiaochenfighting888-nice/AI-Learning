# 数据抽象（Data Abstraction）

很多现实中的数据并不是一个单独的值，而是由多个值组合而成的。

例如：

```text
日期 = 年 + 月 + 日
地理位置 = 纬度 + 经度
有理数 = 分子 + 分母
```

这种由多个部分组合起来形成的数据，可以看作一个**复合对象（compound object）**。

例如有理数：

```text
3
—
4
```

可以理解为由两个整数组成：

```python
numerator = 3
denominator = 4
```

但是在程序中，我们通常希望把：

```text
3 和 4
```

看成一个整体：

```text
3/4
```

这就引出了**数据抽象（Data Abstraction）**。


---

> 数据抽象的核心思想：将“数据如何表示”和“数据如何使用”分离。
>
> 数据抽象的目的就是：让使用数据的人不需要知道数据内部到底是怎么存储的。

也就是把程序中关于数据的内容分成两个部分：

```text
  数据怎么存
Representation

	 ↓ 抽象屏障

  数据怎么用
    Use
```

## 上层：Use

负责：

```text
如何使用有理数
```

例如：

```python
add_rational
mul_rational
equal_rational
```

这些函数只知道：

```python
rational
numer
denom
```

## 下层：Representation

负责：

```text
有理数内部到底怎么存储
```

例如一种可能的实现：

```python
def rational(n, d):
    return [n, d]

def numer(x):
    return x[0]

def denom(x):
    return x[1]
```

于是：

```python
rational(3, 4)
```

内部实际上是：

```python
[3, 4]
```

但是：

```python
add_rational
mul_rational
equal_rational
```

完全不需要知道这一点。

## 抽象屏障（Abstraction Barrier）

> 抽象屏障把：数据怎么表示和数据怎么使用隔开

### 抽象屏障的分层结构

**Abstraction Barrier（抽象屏障）**用于隔离不同层次的程序实现。

> 核心原则：每一层只使用下一层提供的接口，而不直接依赖更底层的具体实现。

以 `Rational Number ADT` 为例，可以分成下面几层：

```text
		  有理数的使用层
        	   ↓
================================
        Abstraction Barrier
================================
        	   ↓
		有理数 ADT 接口层
        	   ↓
================================
        Abstraction Barrier
================================
               ↓
		有理数的具体表示层
        	   ↓
================================
        Abstraction Barrier
================================
        	   ↓
		 List 的底层实现
```

图片中的三层可以整理为：

|               程序层次                | 把 rational 看成 |                          使用的接口                          |
| :-----------------------------------: | :--------------: | :----------------------------------------------------------: |
|          使用有理数完成计算           |   完整的数据值   | `add_rational`、`mul_rational`、`equal_rational`、`print_rational` |
|      创建有理数、实现有理数运算       |    分子和分母    |                 `rational`、`numer`、`denom`                 |
| 实现有理数的 constructor 和 selectors |    两元素列表    |                    list literal、元素选择                    |
|                更底层                 | list 的内部实现  |                       Python 自身实现                        |

#### 有理数使用层

这一层把：

```python
x
```

直接看成：

```text
一个完整的有理数
```

而不是关心：

```text
x 的分子是什么
x 的分母是什么
x 是不是 list
```

例如：

```python
add_rational(x, y)
mul_rational(x, y)
equal_rational(x, y)
print_rational(x)
```

这些函数的使用者只需要知道：

```text
它们能够对有理数进行什么操作
```

不需要知道有理数内部怎么表示。

#### `ADT` 接口层

这一层需要处理：

```text
numerator
denominator
```

因此通过：

```python
rational(n, d)
numer(x)
denom(x)
```

创建和拆解有理数。

例如：

```python
def add_rational(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)

    return rational(
        nx * dy + ny * dx,
        dx * dy
    )
```

这里知道：

```text
有理数由分子和分母构成
```

但是仍然不知道：

```text
分子和分母具体存在哪里
```

例如它不应该关心 `x` 是：

```python
[n, d]
```

还是：

```python
(n, d)
```

#### 具体表示层

到了这一层，才真正处理数据的存储方式。

例如使用两元素列表：

```python
def rational(n, d):
    return [n, d]

def numer(x):
    return x[0]

def denom(x):
    return x[1]
```

这一层知道：

```text
有理数目前使用两个元素列表表示
```

即：

```python
[numerator, denominator]
```

因此可以使用：

```python
[n, d]
x[0]
x[1]
```

但这些具体实现细节不应该泄露给更高层。

### 抽象屏障的使用原则

> 抽象屏障实际上规定了：某一层程序应该使用哪些操作，以及不应该越过哪些层直接访问数据。
>
> 在当前任务允许的情况下，尽量使用更高层的抽象接口，而不是直接操作底层表示。

例如下面的 `add_rational`：

```python
def add_rational(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)

    return rational(nx * dy + ny * dx, dx * dy)
```

这是正确的抽象方式，因为它只通过：

```python
rational
numer
denom
```

操作有理数。

它没有直接访问底层表示。

---

下面这种写法虽然可能运行成功：

```python
def add_rational(x, y):
    return [
        x[0] * y[1] + y[0] * x[1],
        x[1] * y[1]
    ]
```

但它跨越了抽象屏障。

因为 `add_rational` 本来应该处于：

```text
有理数操作层
```

它应该使用：

```python
rational
numer
denom
```

却直接使用了：

```python
x[0]
x[1]
```

这意味着它开始依赖：

```text
有理数使用 list 存储
第 0 个元素是分子
第 1 个元素是分母
```

一旦底层表示发生变化，这个函数就会出错。

---

因此抽象屏障的价值在于：

```text
	修改底层实现
        ↓
   只影响当前抽象层
        ↓
  更高层程序保持不变
```

例如：

```python
numer(x)
```

优于：

```python
x[0]
```

不是因为 `x[0]` 本身错误，而是因为在 `Rational ADT` 的上层代码中：`numer(x)` 保留了抽象边界，而 `x[0]` 泄露了内部表示。

## 抽象数据类型（ADT）

> `ADT`：Abstract Data Type（抽象数据类型）

它允许我们：

> 把一个由多个部分组成的数据，当成一个完整的整体进行操作。

例如有理数：

```text
numerator
-----------
denominator
```

虽然内部可能由两个整数构成，但使用它时，可以把它看成一个完整的有理数。

```text
1/2 → (1, 2)
3/4 → (3, 4)
```

而不是每次都去关心：

```text
它是不是 list？
它是不是 tuple？
分子是不是 x[0]？
分母是不是 x[1]？
```

这些属于**内部表示细节**。

## Constructor：构造器

```python
rational(n, d)
```

作用：

> 根据分子 `n` 和分母 `d` 构造一个有理数。

例如：

```python
x = rational(3, 4)
```

此时：

```text
x 表示 3/4
```

注意：

这里暂时不需要知道 `x` 的内部到底是什么。

它可能是：

```python
[3, 4]
```

也可能是：

```python
(3, 4)
```

甚至以后可能是一个对象：

```python
Rational(3, 4)
```

对于使用者来说都不重要。

## Selector：选择器

选择器用于从复合数据中取出某个组成部分。

对于有理数：

```python
numer(x)
```

作用：

```text
返回 x 的分子
```

例如：

```python
x = rational(3, 4)

numer(x)
```

得到：

```python
3
```

---

另一个选择器：

```python
denom(x)
```

作用：

```text
返回 x 的分母
```

例如：

```python
denom(x)
```

得到：

```python
4
```

## 有理数乘法

假设：

```text
     nx
x = ----
     dx

     ny
y = ----
     dy
```

那么：

```text
nx     ny     nx × ny
--  ×  --  =  -------
dx     dy     dx × dy
```

因此代码：

```python
def mul_rational(x, y):
    return rational(
        numer(x) * numer(y),
        denom(x) * denom(y)
    )
```

也可以写成：

```python
def mul_rational(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)

    return rational(nx * ny, dx * dy)
```

这里：

```python
numer(x)
denom(x)
numer(y)
denom(y)
```

都是通过 **selector** 获取数据。

而：

```python
rational(...)
```

通过 **constructor** 创建新的有理数。

## 有理数加法

假设：

```text
     nx
x = ----
     dx

     ny
y = ----
     dy
```

根据分数加法：

```text
nx     ny     nx × dy + ny × dx
--  +  --  =  -----------------
dx     dy          dx × dy
```

因此：

```python
def add_rational(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)

    return rational(
        nx * dy + ny * dx,
        dx * dy
    )
```

例如：

```text
1     1
-  +  -
2     3
```

得到：

```text
1×3 + 1×2
-----------
   2×3
```

也就是：

```text
5
-
6
```

所以：

```python
x = rational(1, 2)
y = rational(1, 3)

add_rational(x, y)
```

表示：

```text
5/6
```

## 判断两个有理数是否相等

对于：

```text
nx     ny
--  =  --
dx     dy
```

当且仅当：

```text
nx × dy = ny × dx
```

所以：

```python
def equal_rational(x, y):
    return (
        numer(x) * denom(y) == numer(y) * denom(x)
    )
```

例如：

```python
x = rational(1, 2)
y = rational(2, 4)

equal_rational(x, y)
```

结果：

```python
True
```



## 使用 `gcd` 自动约分

例如：

```python
from math import gcd

def rational(n, d):
    g = gcd(n, d)
    return [n // g, d // g]

def numer(x):
    return x[0]

def denom(x):
    return x[1]
```

于是：

```python
rational(2, 4)
```

得到：

```python
[1, 2]
```

因为：

```text
gcd(2, 4) = 2
```

所以：

```text
2 ÷ 2 = 1
4 ÷ 2 = 2
```

## 使用函数表示有理数

`ADT` 的内部表示并不一定必须使用列表或元组，也可以使用函数。

> 只要 constructor 和 selector 保持相同的行为，上层代码就不依赖具体表示方式。

```python
def rational(n, d):
    def select(name):
        if name == "n":
            return n
        elif name == "d":
            return d

    return select
```

此时：

```
def numer(x):
    return x("n")

def denom(x):
    return x("d")
```

对于上层的：

```
add_rational
mul_rational
equal_rational
print_rational
```

不需要做任何修改。

