# Scheme

Scheme 程序主要由**表达式（expression）**组成。

常见表达式可以分为：

- 基本表达式（primitive expression）
- 组合式（combination）
- 特殊形式（special form）

例如：

```scheme
2
3.3
#t
+
quotient
```

这些都可以作为基本表达式。

而：

```
(quotient 10 2)
(+ 1 2)
(not #t)
```

属于组合式。

## 基本表达式

### 自求值表达式

数字可以直接求值得到自身：

```scheme
2
```

结果：

```scheme
2
```

这种表达式称为**自求值表达式（self-evaluating expression）**。

也就是说：

```
表达式本身就是它的值
```

### 符号与绑定

Scheme 中：

```scheme
+
quotient
pi
x
```

这些都是**符号（symbol）**。

符号本身通常需要在环境中找到它所绑定的值。

例如 `quotient `绑定到 Scheme 内置的整数除法过程。

因此：

```scheme
(quotient 10 2)
```

相当于：

```
使用 quotient 这个过程
对 10 和 2 进行运算
```

结果：

```
5
```

## 调用表达式

> Scheme 的函数调用采用**前缀表示法（prefix notation）**：

```
(运算符 操作数1 操作数2 ...)
```

例如：

```
(+ 2 3)
```

其中：

```
+      → 运算符
2、3   → 操作数
```

结果：

```
5
```

和 Python：

```
2 + 3
```

表达的是同一类运算，但写法不同。

### 多个参数

Scheme 中一个过程可以接受多个参数：

```scheme
(+ 1 2 3 4)
```

结果：

```
10
```

操作数数量可以是：

```
0 个或多个
```

具体取决于过程本身允许的参数数量。

## 嵌套表达式

> Scheme 可以直接将一个表达式作为另一个表达式的操作数。

例如：

```scheme
(quotient (+ 8 7) 5)
```

求值时：

```scheme
(+ 8 7) → 15

(quotient 15 5) → 3
```

最终结果：

```
3
```

这种结构本质上仍然符合：

```
(operator operand1 operand2 ...)
```

只是某个操作数本身也是一个组合式。

## 复杂表达式的阅读

```scheme
(+ (* 3
      (+ (* 2 4)
         (+ 3 5)))
   (+ (- 10 7)
      6))
```

阅读 Scheme 表达式时，可以按照括号层级**从内向外**分析。

例如：

```scheme
(+ 3 5)
```

先计算得到：

```
8
```

然后继续代入外层表达式。

分析复杂 Scheme 代码时，比从左到右硬读更有效的方法是：

```
先找到最内层括号
→ 求值
→ 将结果代入外层
→ 逐层向外
```

## 空白与换行

只要括号结构正确，空格和换行通常不会影响表达式含义。

下面两种写法等价：

```
(+ 1 2)
(+ 
   1
   2)
```

复杂表达式经常通过换行和缩进增强可读性。

因此 Scheme 中真正决定结构的是：

```
括号
```

而不是：

```
缩进
```

缩进主要是为了方便人阅读。

## 特殊形式

并不是所有带括号的表达式都是普通函数调用。

某些组合式具有特殊的求值规则，称为**特殊形式（special form）**。

例如：

```
if
and
or
define
```

普通函数调用通常会先求值所有操作数。

特殊形式则可以决定：

```
哪些子表达式求值
哪些子表达式不求值
如何建立新的绑定
```

因此不能简单按照普通函数调用理解。

### if 表达式

基本形式：

```
(if predicate consequent alternative)

    predicate    = 条件表达式
    consequent   = 条件为真时求值的表达式
    alternative  = 条件为假时求值的表达式

           predicate
          条件成立吗？
          /        \
       真            假
       ↓             ↓
consequent      alternative
  真分支            假分支
```

求值过程：

```
1. 先求值 predicate
2. 根据结果，只选择一个分支求值
```

> Scheme中只有 `#f` 被认为是假值，除了 `#f` 以外的其他值通常都认为是真值。
>
> 0、1、-1、“hello”等都是真值。

如果条件为真：

```scheme
(if #t 1 2)
```

只求值：

```scheme
1
```

结果：

```
1
```

如果条件为假：

```scheme
(if #f 1 2)
```

只求值：

```scheme
2
```

结果：

```
2
```

> `if` 不会同时求值 consequent 和 alternative。

### and 与 or

基本形式：

```scheme
(and expression1 expression2 ...)
(or expression1 expression2 ...)
```

它们具有**短路求值（short-circuit evaluation）**的特点。

#### and

> `and` 从左到右依次求值。
>
> 如果遇到假值，就立即停止。
>
> `and` 不一定返回布尔值。
>
> 如果中途遇到 `#f`，整个表达式返回 `#f`。
>
> 如果所有表达式都是真值，则返回最后一个表达式的值。 例如：`(and 1 2 3)` 结果为3。

例如：

```scheme
(and #t #t #f (+ 1 2))
```

遇到：

```scheme
#f
```

以后，后面的：

```scheme
(+ 1 2)
```

不会再求值。

#### or

> `or` 也从左到右依次求值。
>
> 如果已经得到真值，就可以停止后续求值。
>
> `or` 会返回第一个为真的值，而不一定返回 `#t`。

```scheme
(or #f 3 4)
```

结果：

```
3
```

得到第一个真值后，后面的 `4` 不再求值。

`and` 和 `or` 与普通函数调用不同：

```
它们不会无条件求值全部操作数
```

### define 名称绑定

> `define` 可以将一个符号绑定到某个值。

基本形式：

```
(define symbol expression)
```

例如：

```scheme
(define pi 3.14)
```

表示在当前环境中建立：

```
pi → 3.14
```

之后：

```scheme
(* pi 2)
```

就相当于：

```scheme
(* 3.14 2)
```

得到：

```
6.28
```

这和 Python：

```
pi = 3.14
```

作用类似。

## 过程定义

基本形式：

```scheme
(define (name parameter1 parameter2 ...)
  body)
```

例如：

```
(define (square x)
  (* x x))
```

表示：

```
    创建一个过程
		↓
	 参数为 x
		↓
  函数体为 (* x x)
		↓
将这个过程绑定到 square
```

调用：

```
(square 5)
```

得到：

```
25
```

### 多参数过程

可以定义多个参数：

```scheme
(define (add x y)
  (+ x y))
```

调用：

```scheme
(add 3 4)
```

相当于：

```
x → 3
y → 4
```

然后求值：

```scheme
(+ x y)
```

结果：

```
7
```

### 条件过程

```scheme
(define (abs x)
  (if (< x 0)
      (- x)
      x))
```

调用：

```scheme
(abs -3)
```

执行过程：

```
x = -3

(< x 0)
   ↓
  #t
```

所以选择：

```scheme
(- x)
```

即：

```
(- -3)
```

结果为：

```
3
```

## Lambda 表达式

> `lambda` 表达式用于创建**匿名过程（anonymous procedure）**，也就是没有立即绑定名称的函数。
>
> `lambda` 表达式本身不会执行过程体，而是创建一个过程。只有这个过程被调用时，过程体才会求值。

基本形式：

```scheme
(lambda (参数...) 过程体)
```

例如：

```scheme
(lambda (x) (+ x 4))
```

### lambda 与 define

下面两种定义方式效果相同：

```scheme
(define (plus4 x)
  (+ x 4))
```

和：

```scheme
(define plus4
  (lambda (x)
    (+ x 4)))
```

第二种写法更清楚地体现了 `define` 的作用：

```
	先创建一个过程
		↓
再把这个过程绑定到名字 plus4
```

也就是说 `(lambda (x) (+ x 4))` 负责创建过程，`define` 负责把名字 `plus4` 绑定到这个过程。

### 匿名过程的直接调用

Scheme 调用表达式的一般形式是：

```
(operator operand1 operand2 ...)
```

这里的 `operator` 不一定必须是一个名字，它也可以是一个能够求值得到过程的表达式。

例如：

```
((lambda (x) (+ x 4)) 3)
```

先求值：

```scheme
(lambda (x) (+ x 4))
```

得到一个过程，然后用参数：

```
3
```

调用它。

相当于：

```scheme
(+ 3 4)
```

结果：

```
7
```

### 多参数 lambda

`lambda` 可以有多个参数：

```scheme
(lambda (x y z)
  (+ x y (square z)))
```

可以直接调用：

```
((lambda (x y z)
   (+ x y (square z)))
 1 2 3)
```

调用时建立参数绑定：

```
x → 1
y → 2
z → 3
```

然后求值过程体：

```scheme
(+ x y (square z))
```

即：

```scheme
(+ 1 2 (square 3))
```

如果：

```
(square 3)
```

得到 `9`，最终结果就是：

```
12
```

## cond 条件表达式

`cond` 是一个特殊形式，用于处理多个条件分支，作用类似 Python 中的：

```
if ...elif ...else ...
```

基本形式：

```
(cond
  (条件1 表达式1)
  (条件2 表达式2)
  ...
  (else 默认表达式))
```

`else` 通常放在 `cond` 的最后一个分支，表示前面的条件都不成立时就执行 `else` 后面的表达式。

例如：

```scheme
(cond
  ((> x 10) (print 'big))
  ((> x 5)  (print 'medium))
  (else     (print 'small)))
```

> `'big` 表示把 `big` 作为符号本身使用，而不是去环境中查找名字 `big` 所绑定的值。是 `(quote big)` 的简写。
>
> `quote` 作用是不要求值，直接返回后面的东西本身。

对应：

```python
if x > 10:
	print('big')
elif x > 5:
	print('medium')
else:
	print('small')
```

### cond 的求值顺序

`cond` 会从上到下依次检查条件：

```
条件1
 ↓
为真 → 求值对应表达式并结束

为假
 ↓
条件2
 ↓
...
```

例如：

```scheme
(cond
  ((> x 10) 'big)
  ((> x 5) 'medium)
  (else 'small))
```

如果：

```
x = 8
```

那么：

```scheme
(> x 10)
```

为假，继续检查：

```scheme
(> x 5)
```

为真，于是整个 `cond` 的值是符号`medium`

后面的 `else` 不再求值。

### cond 的返回值

`cond` 本身也是一个表达式，因此它可以产生一个值。

```scheme
(print
  (cond
    ((> x 10) 'big)
    ((> x 5) 'medium)
    (else 'small)))
```

各个分支中的：

```
'big
'medium
'small
```

分别求值得到符号：

```
big
medium
small
```

cond 返回其中一个符号值，然后外层 `print` 再打印这个结果。

相比于：

```scheme
(cond
  ((> x 10) (print 'big))
  ...)
```

这两种写法的区别在于：

```
第一种：每个分支自己执行 print

第二种：cond 先产生一个值，再统一交给 print
```

## begin 表达式

> `begin` 用于把多个表达式组合成一个整体。

基本形式：

```scheme
(begin
  表达式1
  表达式2
  ...
  表达式n)
```

这些表达式按照从上到下的顺序依次求值。

例如：

```
(begin
  (print 'big)
  (print 'guy))
```

会依次打印：

```
big
guy
```

### begin 的返回值

> `begin` 不只是“连续执行几条语句”，它本身也是一个表达式，它的值是最后一个表达式的值。

例如：

```scheme
(begin
  (+ 1 2)
  (* 3 4))
```

先计算：

```scheme
(+ 1 2)
```

得到 `3`。

再计算：

```scheme
(* 3 4)
```

得到 `12`。

整个 `begin` 的值为：

```
12
```

### begin 与条件分支

> 当一个条件分支中需要执行多个表达式时，可以使用 `begin`。

例如 Python：

```python
if x > 10:
	print('big')
	print('guy')
else:
	print('small')
	print('fry')
```

Scheme 可以写成：

```scheme
(if (> x 10)
    (begin
      (print 'big)
      (print 'guy))
    (begin
      (print 'small)
      (print 'fry)))
```

这里 `if` 的 consequent 和 alternative 原本各自只能放一个表达式。

使用 `begin` 之后，就可以把多个表达式组合成一个整体。

## cond 与 begin

> `cond` 的一个分支本身可以包含多个表达式，因此这里并不一定需要 `begin`。
>
> `begin` 更重要的用途是在原本只允许放一个表达式的位置，把多个表达式组合成一个表达式。

```scheme
(cond
  ((> x 10)
   (print 'big)
   (print 'guy))
  (else
   (print 'small)
   (print 'fry)))
```

可以理解为：

```
cond：负责选择并求值满足条件的分支。

begin：在原本只能放一个表达式的位置，把多个表达式组合成一个整体。
```

## let 表达式

> `let` 是一个特殊形式，用于建立**临时的局部绑定**。

基本形式：

```scheme
(let ((名字1 值1)
      (名字2 值2)
      ...)
  表达式)
```

例如：

```
(let ((a 3)
      (b 4))
  (+ a b))
```

在这个表达式内部：

```
a → 3
b → 4
```

所以结果为：

```
7
```

### let 的局部作用域

> `let` 创建的名称只在`let` 的主体（body）中有效。

例如：

```scheme
(let ((a 3)
      (b 4))
  (+ a b))
```

在 `let` 内：

```
a、b 可以使用
```

当 `let` 求值结束后：

```
a、b 的临时绑定消失
```

不会像：

```scheme
(define a 3)
```

那样在外部环境中一直存在。

因此 `let` 很适合存放：

```
只在某一次计算过程中使用的中间变量
```

### let 与 define 的区别

使用 `define`：

```scheme
(define a 3)
(define b (+ 2 2))
(define c
  (sqrt (+ (* a a)
           (* b b))))
```

这里：

```
a
b
c
```

都会继续存在于当前环境中。

而：

```scheme
(define c
  (let ((a 3)
        (b (+ 2 2)))
    (sqrt (+ (* a a)
             (* b b)))))
```

其中a、b只在 `let` 内部存在。

`let` 结束后，外部只留下c。

因此：

```
define → 建立持续存在的绑定

let → 建立临时的局部绑定
```

### let 的求值过程

例如：

```scheme
(let ((a 3)
      (b (+ 2 2)))
  (sqrt (+ (* a a)
           (* b b))))
```

首先计算各个绑定右侧的表达式：

```scheme
3
```

得到3。

```scheme
(+ 2 2)
```

得到：

```
4
```

然后建立新的局部环境：

```
a → 3
b → 4
```

最后在这个环境中求值：

```scheme
(sqrt (+ (* a a)
         (* b b)))
```

即：

```scheme
(sqrt (+ 9 16))
```

得到：

```
5
```

### let 绑定的同时性

> `let` 中各个绑定右侧的表达式，通常是在**外层环境**中求值的，然后一起建立新的局部绑定。

例如：

```
(let ((x 2)
      (y x))
  ...)
```

这里 `y` 右边的 `x` 不会自动引用同一个 `let` 中刚刚写出的：

```
x → 2
```

它会尝试从外层环境中查找 `x`。

因此不要把普通 `let` 理解成：

```
先绑定 x，再利用新的 x 绑定 y
```

而应理解成：

```
先分别计算所有右侧表达式
	  ↓
再同时建立局部绑定
	  ↓
求值 let 的主体
```