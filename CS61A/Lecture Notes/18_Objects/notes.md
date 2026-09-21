# 面向对象编程

> 面向对象编程（Object-Oriented Programming，OOP）是一种组织程序的方式。
>
> 面向对象编程的核心思想：将数据和操作数据的方法绑定在一起，让对象自己管理自己的状态。

它建立在数据抽象的基础上，把：

- 数据
- 与数据相关的行为

组织到同一个对象中。

> 对象不仅保存自己的数据，也可以提供操作这些数据的方法。

例如一个列表既保存元素，也提供 `append()`、`pop()` 等操作列表的方法。

## 类（class）

> 类（class）用于描述一类对象的共同特征和行为。

一个类通常定义：

- **属性（attribute）**：对象保存的数据
- **方法（method）**：对象可以执行的操作

例如银行账户：

每个账户都有：

- 账户持有人 `holder`
- 余额 `balance`

同时所有账户都有：

- 存款方法 `deposit`
- 取款方法 `withdraw`

因此可以设计一个 `Account` 类。

```python
class Account:
    ...
```

类描述的是规则，而真正使用的是类创建出来的对象。

### 类与实例

> 通过类创建出来的具体对象称为实例（instance）

~~~text
 类
 ↓ 创建
对象 / 实例
~~~

通过 `type(对象名)` 查看对象类型。

例如：

```python
a = Account("John")
```

这里：

- `Account` 是类
- `a` 是 Account 类的一个实例

可以创建多个实例：

```python
a = Account("John")

b = Account("Jack")
```

虽然它们来自同一个类，但它们是不同的对象。

### 属性

> 对象保存的数据称为属性。

例如：

```python
a.holder
```

访问账户持有人：

```
'John'
```

~~~
a.balance
~~~

访问余额：

```
0
```

这里：

```
holder
balance
```

都是实例属性。

不同实例拥有自己的属性：

```python
a = Account("John")
b = Account("Jack")
```

其中：

```
a.holder → John

b.holder → Jack
```

互不影响。

#### 实例属性修改

对象属性可以通过点号访问和修改。

例如：

```python
a.balance
```

得到：

```
0
```

修改：

```python
a.balance = 12
```

之后：

```python
a.balance
```

结果：

```
12
```

#### 动态添加属性

> 对象可以在创建后添加新的属性。
>
> 普通 Python 对象通常允许动态添加属性。 是否允许取决于对象的实现方式，例如使用 `__slots__` 的类可能限制动态属性。

例如：

```python
a.backup = b
```

此时对象 `a` 新增：

```
backup
```

属性。

访问：

```python
a.backup.balance
```

可以得到：

```
20
```

说明 Python 对象属性具有动态性。

### 方法

> 定义在类中的函数称为方法。

例如：

```python
def deposit(self, amount):
    self.balance = self.balance + amount
    return self.balance
```

方法用于描述对象可以执行的行为。

调用：

```python
a.deposit(15)
```

表示：给账户 a 存入 15。

执行后：

```
balance: 0 → 15
```

### `__init__` 方法

> `__init__` 是一个特殊方法，用于初始化对象。
>
> `__init__` 不是负责创建对象的方法，而是在对象创建后初始化对象属性的方法。

当创建实例时：

```python
a = Account("Alan")
```

Python 会自动调用：

```python
__init__()
```

完成对象初始化。

例如：

```python
class Account:

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
```

执行：

```python
a = Account("Alan")
```

相当于：

1. 创建一个新的 Account 对象
2. 调用 `__init__`
3. 给对象添加属性

最终：

```
Account实例:

holder: "Alan"

balance: 0
```

### self 参数

> `self` 表示：当前正在调用方法的那个实例对象。

例如：

```python
def deposit(self, amount):
    self.balance += amount
```

调用：

```python
a.deposit(10)
```

实际上类似于：

```python
Account.deposit(a, 10)
```

其中：

```
self → a
amount → 10
```

所以方法可以通过：

```python
self.balance
```

访问当前对象自己的属性。

### 点号表达式调用方法

对象通过点号访问属性和方法：

```
对象.属性

对象.方法()
```

例如：

```python
a.balance

a.deposit(10)
```

调用方法时，Python 会自动把对象作为第一个参数传入。

例如定义：

```python
def deposit(self, amount):
```

调用：

```python
a.deposit(10)
```

实际传入：

```python
self = a
amount = 10
```

因此方法能够修改对象自身的数据。

## 对象身份

> 每个实例对象都有唯一身份。

例如：

```
a = Account("John")

b = Account("Jack")
```

虽然：

```
a
b
```

都是 Account 实例，但是它们是不同对象。

### is 运算符

> `is` 用于判断两个变量是否指向同一个对象。
>
> 通常比较对象内容是否相等时使用 `==`，判断是否同一个对象时使用 `is`。

例如：

```python
a is a
```

结果：

```python
True
```

因为两个引用指向同一个对象。

------

```python
a is b
```

结果：

```
False
```

因为：

```python
a → Account("John")

b → Account("Jack")
```

是两个不同实例。

### 赋值不会创建新对象

例如：

```python
c = a
```

并不会创建新的 Account 对象。

而是：

```text
a → 同一个对象 ← c
```

所以：

```python
c is a
```

结果：

```python
True
```
