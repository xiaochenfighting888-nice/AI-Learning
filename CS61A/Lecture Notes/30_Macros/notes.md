# Scheme 宏

> 宏（Macro）用于在真正求值之前，对程序的源代码进行转换。
>
> 宏把原始程序转换成另一段程序的过程称为**宏展开（Macro Expansion）**。

可以把它理解成：

```text
	 原始代码
		↓
	  宏展开
		↓
生成新的 Scheme 表达式
		↓
  再对生成的表达式求值
```

宏本质上是在做：代码到代码的转换。

## define-macro

> 这里介绍的是 CS61A Scheme 提供的 `define-macro`。不同 Scheme 实现的宏系统和语法可能不同。

```scheme
(define-macro (名称 参数...)
  宏体)
```

例如：

```scheme
(define-macro (twice expr)
  (list 'begin expr expr))
```

这个宏的作用是：

```
 接收一段表达式 expr
		↓
 把这段表达式复制两次
		↓
生成一个 begin 表达式
```

例如：

```
(twice (print 2))
```

第一步，求值运算符：

```
twice
```

发现它对应的是一个宏。

第二步，不求值操作数：

```
(print 2)
```

直接把这个表达式传给宏。

所以：

```
   expr
	↓
(print 2)
```

第三步，执行宏体：

```scheme
(list 'begin expr expr)
```

得到：

```
(begin
  (print 2)
  (print 2))
```

然后解释器再对这个返回的表达式求值。

最终：

```
2
2
```

## 普通函数与宏的区别

```
普通函数 → 先求值参数，再调用函数

宏
→ 参数先不求值
→ 直接把参数表达式交给宏
→ 宏生成新的代码
→ 再执行生成的代码
```

考虑普通函数：

```scheme
(define (twice expr)
  (list 'begin expr expr))
```

然后调用：

```
(twice (print 2))
```

由于这是普通函数，所以 Scheme 会先求值参数：

```
(print 2)
```

因此先输出：

```
2
```

而 `expr` 得到的已经不是：

```
(print 2)
```

这个表达式，而是 `print` 的返回值。

所以最后结果：

```
(begin undefined undefined)
```

也就是说：普通函数拿到的是表达式求值后的结果，而不是表达式本身。

## 普通函数使用 quote 绕过提前求值

如果普通函数确实想接收表达式本身，可以手动引用：

```scheme
(twice '(print 2))
```

这样：

```
expr
```

得到：

```
(print 2)
```

函数返回：

```scheme
(begin
  (print 2)
  (print 2))
```

但此时它仍然只是一个列表，并没有执行。

因此还需要：

```scheme
(eval (twice '(print 2)))
```

才会真正输出：

```
2
2
```

所以普通函数需要：

```
quote + 函数调用 + eval
```

而宏可以直接：

```scheme
(twice (print 2))
```

## 使用准引用定义宏

生成复杂 Scheme 表达式时，使用准引用通常比大量 `list` 更容易阅读。

例如：

```scheme
(define-macro (twice expr)
  `(begin ,expr ,expr))
```

和：

```scheme
(define-macro (twice expr)
  (list 'begin expr expr))
```

作用相同。

前者可以直接看到最终想生成的代码结构：

```
(begin
  expr
  expr)
```

其中：

```
,expr
```

表示把宏参数对应的代码插入这里。

因此宏通常会大量使用：

```
`准引用

,取消引用
```

来构造代码模板。

## for 宏

`map` 它会把一个过程应用到列表中的每个元素，并把结果组成新的列表。

一种递归实现：

```scheme
(define (map fn vals)
  (if (null? vals)
      nil
      (cons (fn (car vals))
            (map fn (cdr vals)))))
```

例如：

```scheme
(map (lambda (x) (* x x))
     '(2 3 4 5))
```

执行过程可以理解为：

```text
2 → 2² → 4
3 → 3² → 9
4 → 4² → 16
5 → 5² → 25
```

最终：

```scheme
(4 9 16 25)
```

这里真正决定“每个元素怎么处理”的是：

```scheme
(lambda (x) (* x x))
```

---

定义 for 宏：

```scheme
(define-macro (for sym vals expr)
  (list 'map
        (list 'lambda (list sym) expr)
        vals))
```

因此：

```scheme
(for x '(2 3 4 5) (* x x))
```

得到：

```scheme
(4 9 16 25)
```

首先：

```scheme
(list sym)
```

其中：

```text
sym = x
```

所以得到：

```scheme
(x)
```

接着：

```scheme
(list 'lambda (list sym) expr)
```

代入：

```text
sym  = x
expr = (* x x)
```

得到：

```scheme
(lambda (x) (* x x))
```

注意这里不是执行这个 `lambda`，而是在**构造表示 lambda 表达式的列表**。

最外层：

```scheme
(list 'map
      (list 'lambda (list sym) expr)
      vals)
```

最终生成：

```scheme
(map
  (lambda (x) (* x x))
  '(2 3 4 5))
```

### 使用准引用改写

使用 `list`：

```scheme
(define-macro (for sym vals expr)
  (list 'map
        (list 'lambda (list sym) expr)
        vals))
```

可以使用准引用写得更直观：

```scheme
(define-macro (for sym vals expr)
  `(map
     (lambda (,sym) ,expr)
     ,vals))
```

这里：

```text
` → 整体作为代码模板

,sym → 插入变量名

,expr → 插入处理表达式

,vals → 插入要遍历的列表表达式
```

调用：

```scheme
(for x '(2 3 4 5) (* x x))
```

仍然生成：

```scheme
(map
  (lambda (x) (* x x))
  '(2 3 4 5))
```

对于宏而言，准引用通常更容易直接看出：

```text
最终想生成什么代码
```

# 递归调用追踪

## Python 中的递归调用追踪

可以通过一个高阶函数给原函数增加“打印每次调用”的功能：

```python
def trace(fn):
    def traced(n):
        print(f'{fn.__name__}({n})')
        return fn(n)
    return traced
```

然后使用装饰器：

```python
@trace
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
```

调用：

```python
fact(5)
```

会得到类似：

```text
fact(5)
fact(4)
fact(3)
fact(2)
fact(1)
fact(0)
120
```

这一段：

```python
@trace
def fact(n):
    ...
```

可以理解成：

```python
def fact(n):
    ...

fact = trace(fact)
```

因此名字 `fact` 最终不再直接指向原来的阶乘函数，而是指向：

```text
traced
```

### 递归调用经过包装函数

原来的阶乘函数中写着：

```python
fact(n - 1)
```

虽然这行代码定义在“原来的 `fact`”里面，但运行到这里时，Python 会根据当前环境查找名字：

```text
fact
```

而此时全局的 `fact` 已经重新绑定到了：

```text
traced
```

所以执行过程实际上是：

```text
	  fact(5)
		↓
	  traced(5)
		↓ 打印 fact(5)
	 原 fact(5)
		↓
  里面调用 fact(4)

当前 fact 又是 traced
		↓
	 traced(4)
		↓ 打印 fact(4)
	原 fact(4)
		↓
	   ...
```

因此所有递归调用都能够被追踪到。

## Scheme 中的递归调用追踪

原始阶乘：

```scheme
(define fact
  (lambda (n)
    (if (zero? n)
        1
        (* n (fact (- n 1))))))
```

首先保存原来的过程：

```scheme
(define original fact)
```

此时：

```text
original → 原来的 fact
fact     → 原来的 fact
```

然后重新定义：

```scheme
(define fact
  (lambda (n)
    (print (list 'fact n))
    (original n)))
```

此时：

```text
fact → 新的包装过程

original → 原来的阶乘过程
```

调用：

```scheme
(fact 5)
```

新的 `fact`：

1. 打印 `(fact 5)`
2. 调用 `(original 5)`

进入原来的阶乘函数以后，其中仍然有：

```scheme
(fact (- n 1))
```

注意它调用的是名字：

```scheme
fact
```

而不是 `original`。

此时 `fact` 已经指向包装过程，所以递归又会进入：

```scheme
fact
```

并打印下一次调用。

过程：

```text
	  (fact 5)
		 ↓
	  包装 fact
		 ↓
	打印 (fact 5)
		 ↓
	(original 5)
		 ↓
原阶乘函数内部调用 (fact 4)
		 ↓
	  包装 fact
		 ↓
	 打印 (fact 4)
		 ↓
	 (original 4)
		 ↓
		...
```

因此得到：

```text
(fact 5)
(fact 4)
(fact 3)
(fact 2)
(fact 1)
(fact 0)
120
```

### 使用宏自动完成追踪

如果每次都手动：

```scheme
(define original fact)

(define fact
  (lambda (n)
    ...
    (original n)))
```

会比较麻烦。

可以定义一个宏，让：

```scheme
(trace (fact 5))
```

自动完成这些操作。

> 这个 `trace` 宏只是用于说明宏如何临时修改绑定，并不是通用的追踪工具。
>
> 它目前假设被追踪的过程只有一个参数，并且使用了 `original`、`result`、`n` 等固定辅助名称；如果程序中本来就使用这些名称，可能发生名称冲突。

```scheme
(define-macro (trace expr)
  (define operator (car expr))

  `(begin
     (define original ,operator)

     (define ,operator
       (lambda (n)
         (print (list (quote ,operator) n))
         (original n)))

     (define result ,expr)

     (define ,operator original)

     result))
```

这个宏的作用不是直接计算 `fact(5)`，它是在**生成一段临时修改函数绑定的 Scheme 程序**。

调用：

```scheme
(trace (fact 5))
```

因为 `trace` 是宏，所以：

```scheme
(fact 5)
```

不会提前求值。

因此：

```text
  expr
   ↓
(fact 5)
```

宏得到的是整个表达式本身。

宏中：

```scheme
(define operator (car expr))
```

由于：

```scheme
expr = (fact 5)
```

所以：

```scheme
(car expr)
```

得到：

```scheme
fact
```

因此：

```text
operator → fact
```

对于：

```scheme
(trace (fact 5))
```

宏展开后可以近似看成：

```scheme
(begin

  (define original fact)

  (define fact
    (lambda (n)
      (print (list 'fact n))
      (original n)))

  (define result (fact 5))

  (define fact original)

  result)
```

这才是整个 `trace` 宏真正要做的事情。

可以分成四个阶段理解：

```text
   保存原函数
	  ↓
  临时替换函数
	  ↓
执行要追踪的表达式
	  ↓
   恢复原函数
```

接下来：

```scheme
(define result ,expr)
```

在当前例子中展开为：

```scheme
(define result (fact 5))
```

此时 `fact` 已经临时被替换成了包装函数。

所以：

```scheme
(fact 5)
```

会经过追踪。

整个递归过程中，原阶乘函数内部写的是：

```scheme
(fact (- n 1))
```

这些调用也都会重新找到当前临时定义的 `fact`。

因此输出：

```text
(fact 5)
(fact 4)
(fact 3)
(fact 2)
(fact 1)
(fact 0)
```

最终：

```text
result → 120
```

追踪结束后：

```scheme
(define fact original)
```

把 `fact` 恢复为原来的过程：

```text
   fact
	↓
原来的 fact
```

所以之后再次执行：

```scheme
(fact 5)
```

只得到：

```text
120
```

不会再打印递归调用。

这说明这个宏只是：在计算某个表达式期间临时修改 `fact` 的绑定，追踪完成后会恢复原状态。

如果直接：

```scheme
(define fact original)
```

以后再去执行表达式，那么追踪环境已经没了。

所以必须先：

```scheme
(define result (fact 5))
```

在包装函数仍然生效时完成整个计算。

得到结果后：

```text
result = 120
```

再恢复：

```scheme
fact → original
```

最后：

```scheme
result
```

返回保存好的计算结果。
