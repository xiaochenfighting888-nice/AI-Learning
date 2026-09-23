# 字符串表示

> 字符串表示（String Representation）就是：将一个对象转换成字符串形式，方便人类查看或 Python 解释器理解。

Python 中所有对象都有两种主要的字符串表示：

- `str`
- `repr`

二者通常不同，但有时相同。

## eval()

> `eval() ` 就是把“字符串当成代码来运行”，然后返回表达式的结果。

~~~python
eval(expression, globals=None, locals=None)

expression：一个字符串形式的 Python 表达式
globals（可选）：全局命名空间
locals（可选）：局部命名空间
返回值：表达式的执行结果
~~~

~~~python
print("1+2")   # 输出：1+2
eval("1+2")    # 结果：3
~~~

## repr：面向 Python 解释器的表示

`repr(object)` 返回一个字符串：

```python
repr(object) -> string
```

它表示对象的**标准字符串形式（canonical string representation）**。

理想情况下：

```python
eval(repr(object)) == object
```

可以创建一个等价对象。 但很多对象的 repr 主要用于调试，并不保证可以直接 eval。

例如：

```python
>>> repr(12e12)
'12000000000000.0'
```

这个字符串可以被 Python 解释。

### repr 的特点

`repr` 更偏向：

- 给程序员查看
- 调试使用
- 尽可能包含对象的信息

例如：

```python
>>> repr(min)
'<built-in function min>'
```

可以看出：

- 这是一个内置函数
- 名字是 `min`

### 交互式环境默认调用 repr

在 Python 交互环境：

```python
>>> 12e12
12000000000000.0
```

实际上显示的是：

```python
repr(12e12)
```

等价于：

```python
>>> print(repr(12e12))
12000000000000.0
```

### 实现 repr

如果想让自定义对象支持：

```python
repr(obj)
```

需要定义：

```python
__repr__()
```

例如：

```python
class Fraction:

    def __repr__(self):
        return "Fraction(1, 2)"
```

调用：

```
repr(fraction)
```

会返回：

```
Fraction(1, 2)
```

### repr 的查找规则

`repr` 的行为比简单调用：

```
x.__repr__()
```

稍微复杂。

原因：实例属性中的 `__repr__` 会被忽略。

例如：

```python
obj.__repr__ = some_function
```

不会影响：

```python
repr(obj)
```

Python 只会查找：**类（class）中的 `__repr__` 方法**

因此：

```python
repr(x)
```

实际类似：

```python
type(x).__repr__(x)
```

过程：

```
	 对象 x
 	  ↓
  找到 x 的类型
 	  ↓
查找类中的 __repr__
	  ↓
	 调用
```

## str：面向用户的表示

> `str(object)` 返回对象的人类可读形式。

特点：

- 更简洁
- 更容易阅读
- 用于输出展示

例如：

```python
from fractions import Fraction

half = Fraction(1, 2)

>>> repr(half)
'Fraction(1, 2)'

>>> str(half)
'1/2'

>>> eval(repr(half))
Fraction(1, 2)

>>> eval(str(half))
0.5
```

~~~python
eval(repr(half)) 等价于：eval("Fraction(1, 2)")
Python 会：
	1.找到 Fraction
	2.执行 Fraction(1, 2)
	3.返回一个新对象
    
str(half) 结果是："1/2"
eval("1/2") 当成：1 / 2 = 0.5
~~~

### print 默认调用 str

例如：

```python
>>> print(half)
1/2
```

实际上调用：

```python
str(half)
```

### 实现 str

定义：

```python
__str__()
```

即可改变：

```python
str(obj)
```

的结果。

例如：

```python
class Fraction:

    def __str__(self):
        return "1/2"
```

调用：

```python
str(fraction)
```

输出：

```
1/2
```

### str 的特殊规则

> `str(obj)` 查找 `__str__` 的规则类似：
>
> Python 会查找对象所属类中的 `__str__` 方法，
> 而不是实例动态添加的 `__str__` 属性。

`str` 比 `repr` 更复杂：

#### 情况1：存在 **str**

调用：

```python
obj.__str__()
```

#### 情况2：没有 **str**

Python 会使用 `repr` 作为备用。

即：

```python
str(obj)
```

类似：

```python
repr(obj)
```

------

例如：

```python
class A:

    def __repr__(self):
        return "A object"
```

没有定义：

```python
__str__
```

那么：

```python
str(A())
```

仍然可以得到：

```python
A object
```

# 字符串插值（String Interpolation）

> 字符串插值指：在字符串中直接嵌入表达式的值。

常用于格式化输出。

## 使用字符串拼接

传统方式：

```python
from math import pi

'pi starts with ' + str(pi) + '...'
```

过程：

1. 将 `pi` 转换为字符串
2. 和其他字符串拼接

结果：

```
pi starts with 3.141592653589793...
```

缺点：

- 代码较长
- 可读性差
- 多个变量时容易混乱

## f-string 字符串插值

语法：

```python
f"文本{表达式}"
```

例如：

```python
from math import pi

f'pi starts with {pi}...'
```

输出：

```
pi starts with 3.141592653589793...
```

## f-string 的执行过程

对于：

```python
f'Value is {x}'
```

Python 会：

1. 计算 `{x}` 中的表达式
2. 使用该值的 `str` 表示
3. 替换到字符串中

例如：

```python
x = 10

f'value = {x}'
```

等价于：

```python
'value = ' + str(x)
```

## f-string 可以包含任意表达式

例如：

```python
name = "Tom"
age = 20

f"{name} is {age} years old"
```

结果：

```
Tom is 20 years old
```

# 特殊方法（Special Methods）

Python 中有一些特殊的方法名，它们具有内置行为。

特点：

- 方法名以两个下划线 `__` 开头
- 以两个下划线 `__` 结尾

形式：

```python
__method__
```

这些方法通常不会被直接调用，而是由 Python 在特定操作时自动调用。

例如：

```python
a + b
```

实际上会调用：

```python
a.__add__(b)
```

## 常见特殊方法

|  特殊方法   |                作用                |
| :---------: | :--------------------------------: |
| `__init__`  | 创建对象时自动调用，用于初始化对象 |
| `__repr__`  |     返回对象的 Python 表达形式     |
|  `__add__`  |       定义对象之间的加法行为       |
| `__bool__`  |  定义对象转换为 True/False 的行为  |
| `__float__` |     定义对象转换为浮点数的行为     |

## 特殊方法与普通操作的关系

Python 的语法糖：

## 加法

普通写法：

```
one + two
```

等价于：

```
one.__add__(two)
```

------

## 布尔转换

普通写法：

```
bool(one)
```

等价于：

```
one.__bool__()
```

------

因此：

> 运算符和内置函数，本质上都是调用对象对应的特殊方法。

# 接口（Interfaces）

接口规定：

- 有哪些方法
- 方法应该完成什么功能

但不规定：

- 具体如何实现

比如：

```python
str(obj)
```

要求对象提供：

```python
__str__()
```

这就是接口。

不同类：

```python
Fraction.__str__()
Ratio.__str__()
```

实现不同。

但是：

```python
str(obj)
```

都可以工作。

# 多态函数（Polymorphic Function）

> 多态函数：一个可以作用于多种不同形式（different forms）数据的函数。

即：**同一个函数名，可以处理不同类型的对象，并表现出不同的行为。**

例如：

```python
str(obj)
repr(obj)
```

都属于多态函数，因为它们可以作用于任意对象。

## str 和 repr 的多态性

`str` 和 `repr` 都可以接受任何对象：

```python
str(object)
repr(object)
```

但是它们具体执行什么行为，取决于对象所属的类。

例如：

```python
half = Fraction(1, 2)
```

调用：

```python
repr(half)
```

实际上会调用：

```python
half.__repr__()
```

结果：

```python
'Fraction(1, 2)'
```

------

调用：

```python
str(half)
```

实际上会调用：

```python
half.__str__()
```

结果：

```
'1/2'
```

