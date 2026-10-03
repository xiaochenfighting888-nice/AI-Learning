# 代码即数据

Scheme 程序由表达式组成。

基本表达式包括：

```scheme
2
3.3
true
+
quotient
```

组合式例如：

```
(quotient 10 2)
(not true)
```

Scheme 一个非常重要的特点是：

> Scheme 的组合表达式本身可以用 Scheme 列表来表示。

例如：

```
(quotient 10 2)
```

既可以被理解成一段程序：

```
调用 quotient
参数为 10 和 2
```

也可以被构造成一个普通列表：

```
(list 'quotient 10 2)
```

得到：

```
(quotient 10 2)
```

所以在 Scheme 中，程序代码和列表数据可以具有相同的表示形式。

```scheme
(+ 1 2)
```

作为程序：

```
执行加法 → 3
```

而：

```scheme
'(+ 1 2)
```

作为数据：

```
(+ 1 2)
```

这个数据又可以：

```scheme
(car '(+ 1 2))
```

取出：

```
+
```

或者：

```scheme
(eval '(+ 1 2))
```

重新执行：

```
→ 3
```

因此：

```
Scheme 代码可以用 Scheme 的数据结构来表示，因此程序可以把代码作为数据进行构造和操作。
```

# `eval`

> `eval` 用于把一个表示 Scheme 表达式的数据结构，当作真正的 Scheme 代码进行求值。

例如：

```scheme
(list 'quotient 10 2)
```

首先只是创建列表：

```
(quotient 10 2)
```

此时并没有进行除法。

再执行：

```scheme
(eval (list 'quotient 10 2))
```

解释器会把：

```
(quotient 10 2)
```

当成 Scheme 表达式执行。

得到：

```
5
```

可以把这一过程理解成：

```
代码
 ↓ quote / list 等方式
数据

  数据
   ↓ eval
代码执行
```

例如：

```scheme
'(+ 1 2)
```

得到的是数据：

```
(+ 1 2)
```

而：

```scheme
(eval '(+ 1 2))
```

才真正执行：

```
(+ 1 2)
```

得到：

```
3
```

因此：

```
quote → 不对表达式进行正常求值，而是把表达式作为数据得到

eval  → 对表示表达式的数据进行求值，把它作为代码执行
```

# 生成 Scheme 表达式

因为 Scheme 表达式可以用列表表示，所以程序本身可以**构造另外一段程序**。

例如阶乘：

```scheme
(define (fact n)
  (if (= n 0)
      1
      (* n (fact (- n 1)))))
```

普通 `fact` 直接计算结果。

还可以写返回表达式的阶乘函数：

```scheme
(define (fact-exp n)
  (if (= n 0)
      1
      (list '* n (fact-exp (- n 1)))))
```

这里不是直接做乘法，而是构造表示乘法的列表。

例如：

```scheme
(fact-exp 3)
```

得到类似：

```
(* 3 (* 2 (* 1 1)))
```

此时得到的是表示计算过程的 Scheme 表达式，而不是计算结果。

再执行：

```scheme
(eval (fact-exp 3))
```

才会得到：

```
6
```

## Fibonacci 表达式生成

普通 Fibonacci：

```scheme
(define (fib n)
  (if (<= n 1)
      n
      (+ (fib (- n 2))
         (fib (- n 1)))))
```

直接返回 Fibonacci 数值。

------

可以写一个生成表达式的版本：

```scheme
(define (fib-exp n)
  (if (<= n 1)
      n
      (list '+
            (fib-exp (- n 2))
            (fib-exp (- n 1)))))
```

例如：

```scheme
(fib-exp 4)
```

得到的不是 `3`，而是类似：

```
(+ (+ 0 1)
   (+ 1 (+ 0 1)))
```

这个列表描述了计算 `fib(4)` 所需要进行的加法。

执行：

```scheme
(eval (fib-exp 4))
```

才得到：

```
3
```

所以这里存在两种不同的函数：

```
fib → 直接计算结果

fib-exp  生成一段能够计算结果的 Scheme 程序
```

## 程序生成程序

这是 Scheme 非常有代表性的能力：

```
 程序 A
   ↓
  运行
   ↓
生成程序 B
   ↓
  eval
   ↓
执行程序 B
```

也就是：程序可以把程序本身作为数据进行构造和操作。

# 准引用（`quasiquote`）

普通引用：

```scheme
'(a b)
```

得到：

```
(a b)
```

准引用使用反引号：

```scheme
`(a b)
```

同样得到：

```
(a b)
```

如果里面没有特殊标记，它们看起来没有区别。

# 取消引用（unquote） 

> 准引用最大的区别是：可以让其中某些部分恢复正常求值。
>
> `,`（unquote）只有放在准引用 `` ` `` 的结构内部时，才具有“恢复求值”的含义。

使用逗号：

```
,
```

表示取消引用（unquote），用于把动态内容插入模板。

假设：

```scheme
(define b 4)
```

执行：

```scheme
`(a ,(+ b 1))
```

其中：

```
a
```

仍然作为符号保存。

但是：

```scheme
,(+ b 1)
```

会先进行求值：

```
(+ 4 1) → 5
```

所以结果：

```
(a 5)
```

# quote 与准引用的区别

如果使用普通 `quote`：

```scheme
'(a ,(+ b 1))
```

不会让：

```scheme
(+ b 1)
```

得到 `5`。

因为整个内容都被引用起来了。

而：

```scheme
`(a ,(+ b 1))
```

允许通过：

```
,
```

指定某一部分需要求值。

可以记成：

```
' → 整体不求值

` → 默认不求值

, → 在准引用内部恢复这一部分的求值
```

# 准引用构造代码

准引用特别适合生成 Scheme 程序。

例如：

```scheme
(define (make-add-procedure n)
  `(lambda (d) (+ d ,n)))
```

调用：

```scheme
(make-add-procedure 2)
```

其中：

```
,n
```

会被当前 `n` 的值替换。

因此得到：

```scheme
(lambda (d) (+ d 2))
```

这里得到的仍然是一个表示程序的列表。

如果进一步：

```
(eval (make-add-procedure 2))
```

就可以得到一个真正可调用的过程。

# 用递归表示 while 循环

Scheme 中可以使用递归来表达循环过程，其中尾递归可以实现类似 Python `while` 循环的迭代计算。

例如 Python：

```python
x = 2
total = 0

while x < 10:
	total = total + x * x
	x = x + 2
```

计算：

```
2² + 4² + 6² + 8² = 120
```

Scheme 可以写成：

```scheme
(begin

  (define (f x total)
    (if (< x 10)
        (f (+ x 2)
           (+ total (* x x)))
        total))

  (f 2 0))
```

## 泛化代码生成器

可以进一步写一个过程，让它**生成这种递归程序**：

```scheme
(define (sum-while initial-x condition add-to-total update-x)
  `(begin

     (define (f x total)
       (if ,condition
           (f ,update-x
              (+ total ,add-to-total))
           total))

     (f ,initial-x 0)))
     
initial-x → 初始 x
condition → 是否继续循环
add-to-total → 每次累加什么
update-x → 每次如何更新 x
```

这里：

```
整个 begin / define / if / f 的结构
```

是固定模板。

而：

```
,initial-x
,condition
,add-to-total
,update-x
```

是动态插入的部分。

例如：

```scheme
(sum-while
  1
  '(< (* x x) 50)
  'x
  '(+ x 1))
```

生成：

```scheme
(begin

  (define (f x total)
    (if (< (* x x) 50)
        (f (+ x 1)
           (+ total x))
        total))

  (f 1 0))
```

注意：sum-while这里只是在生成程序，它本身并没有执行这个循环。

## `eval` 执行生成的程序

假设：

```scheme
(define result
  (sum-while
    1
    '(< (* x x) 50)
    'x
    '(+ x 1)))
```

此时：

```
result
```

是一个 Scheme 列表：

```scheme
(begin
  (define (f x total)
    ...)
  (f 1 0))
```

所以：

```scheme
(list? result)
```

会得到：

```
#t
```

它确实只是一个列表。

甚至：

```scheme
(car result)
```

会得到：

```scheme
begin
```

说明这个列表的第一个元素就是符号：

```scheme
begin
```

------

然后：

```scheme
(eval result)
```

解释器才真正把这个列表作为 Scheme 程序执行。

最终得到：

```
28
```

因为：

```
1² < 50
2² < 50
...
7² < 50

1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
```

## 同一模板生成不同循环

> 一个程序生成器可以根据不同参数生成不同程序。

例如：

```
(eval
  (sum-while
    2
    '(< x 10)
    '(* x x)
    '(+ x 2)))
```

对应：

```
x = 2
total = 0

while x < 10:
    total = total + x * x
    x = x + 2
```

最终：

```
2² + 4² + 6² + 8² = 120
```

调用：

```
(sum-while
  2
  '(< x 10)
  '(* x x)
  '(+ x 2))
```

这里很多参数前面使用：

```
'
```

原因是这些参数不是现在就要执行，而是要作为**代码数据**传入。

例如：

```
'(< x 10)
```

表示：不要现在判断 x < 10，而是把 `(< x 10)` 这个表达式本身传给 `sum-while`。

之后 `sum-while` 再把它插入生成的程序中。