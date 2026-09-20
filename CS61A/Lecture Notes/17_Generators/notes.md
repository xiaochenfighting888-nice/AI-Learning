# 生成器函数

> 生成器函数（generator function）是一种特殊的函数，它使用 `yield` 产生值，而不是只通过 `return` 返回结果。
>
> `yield` 和 `return` 最大的区别在于：
>
> - `return` 返回结果后，函数执行结束
> - `yield` 产生一个结果后，函数只是暂时停止，并保存当前执行状态

例如：

```python
def plus_minus(x):
    yield x
    yield -x
```

只要函数体中出现 `yield`，这个函数就属于生成器函数。

普通函数通常执行到 `return` 后就结束，而生成器函数可以执行到多个 `yield`，分多次产生结果。

## 生成器函数的调用

调用普通函数：

```python
result = f()
```

通常会立即执行函数体并得到返回值。

调用生成器函数：

```python
t = plus_minus(3)
```

主要是创建生成器对象，函数体会随着 `next()` 的调用逐步执行。

因此生成器具有前面迭代器学习过的特点：

- 保存当前执行位置
- 每次产生一个值
- 被逐步消耗

# 生成器

> 生成器本质上是一种特殊的迭代器。

调用生成器函数时，不会直接得到 `yield` 后面的值，而是得到一个**生成器（generator）对象**：

```python
t = plus_minus(3)
```

此时 `t` 是一个生成器，同时也是一个迭代器，因此可以使用 `next()`：

```python
next(t) # 3

next(t) # -3
```

可以理解为：

```text
 plus_minus(3)
      ↓
	生成器 t
      ↓ next()
 执行到 yield x
      ↓
 返回 3，并暂停
      ↓ next()
 从暂停处继续执行
      ↓
 执行到 yield -x
      ↓
返回 -3，并再次暂停
```

## 生成器结束

当函数中已经没有更多 `yield` 可以执行时：

```python
next(t)
```

会产生：

```text
StopIteration
```

表示生成器已经迭代结束。

# yield from

> `yield from` 用于：依次产生另一个可迭代对象或迭代器中的所有元素。

例如：

```python
def a_then_b(a, b):
    yield from a
    yield from b
```

调用：

```python
list(a_then_b([3, 4], [5, 6]))
```

结果：

```
[3, 4, 5, 6]
```

执行过程可以理解为：

```
先产生 a 中的所有元素
3
4

再产生 b 中的所有元素
5
6
```

## yield from 与 for 循环

下面两种写法效果相同。

使用普通 `yield`：

```python
def a_then_b(a, b):
    for x in a:
        yield x

    for x in b:
        yield x
```

使用 `yield from`：

```python
def a_then_b(a, b):
    yield from a
    yield from b
```

因此：

```python
yield from iterable
```

可以简单理解为：

```python
for x in iterable:
    yield x
```

`yield from` 可以让代码更加简洁。

## 递归中的 yield from

`yield from` 也可以和递归结合使用。

例如：

```python
def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k - 1)
```

调用：

```
list(countdown(5))
```

结果：

```
[5, 4, 3, 2, 1]
```

执行过程：

```
countdown(5)
    yield 5
    ↓
countdown(4)
    yield 4
    ↓
countdown(3)
    yield 3
    ↓
countdown(2)
    yield 2
    ↓
countdown(1)
    yield 1
```

这里：

```python
yield from countdown(k - 1)
```

表示：把递归调用产生的所有值继续逐个产生出来。

## yield 与 yield from

```python
yield x
```

表示：产生一个值 `x`。

而：

```python
yield from iterable
```

表示：依次产生 `iterable` 中的所有值。

例如：

`yield`：

```python
def f():
    yield [1, 2, 3]
```

调用：

```python
list(f())
```

结果：

```text
[[1, 2, 3]]
```

因为 `yield` 将整个 `[1, 2, 3]` 当作一个值产生。

---

`yield from`：

```python
def g():
    yield from [1, 2, 3]
```

调用：

```python
list(g())
```

结果：

```text
[1, 2, 3]
```

因为 `yield from` 会依次产生可迭代对象中的每一个元素。

