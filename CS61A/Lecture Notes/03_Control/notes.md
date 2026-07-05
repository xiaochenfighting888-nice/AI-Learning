# 多重环境—Multiple Environments

> 程序运行过程中往往存在多个环境：每次函数调用都会创建一个新的局部帧，这个局部帧会指向它的父帧，从而形成用于名字查找的环境链。

![局部截取_20260704_163441](../../images/局部截取_20260704_163441.png)

~~~
环境是由一系列帧组成的。
f1和f2是两个不同的局部帧。
在square(square(3)) 中，会先执行内层square(3)，此时环境是：f1(local) → Global。
内层调用返回结果后，再执行外层square(...)，此时环境是：f2(local) → Global。
每个环境通常只包含从当前帧沿父指针一路到全局帧的那一串帧，而不是程序运行中出现过的所有帧。
从某个帧开始，沿着它的父帧不断向上查找，就形成了一个环境。
~~~

![局部截取_20260704_164924](../../images/局部截取_20260704_164924.png)

~~~
每个表达式都在某个“环境”中求值。
名字求值时，会从当前环境的第一个帧，也就是当前局部帧开始查找；找不到再沿父帧继续查找，直到全局帧。

在f2中，x就在f2里 → 直接找到x=9。
在f2中，mul不在f2里 → 往父帧（Global）找 → 找到mul。
~~~

![局部截取_20260705_111748](../../images/局部截取_20260705_111748.png)

~~~
不同环境，名字可能有不同的含义，因为每个帧中对同一名字可以有不同的绑定。
函数调用表达式（紫色箭头）和被调用函数的函数体（绿色箭头）是在不同的环境中求值的。
	紫色箭头1：指向square(4)的调用，这是在全局环境中开始的，因为这句话在全局脚本中，并没有嵌套在任何其他函数内部。
	绿色箭头2：进入函数体return mul(square, square)的执行，此时进入了f1局部环境。
调用表达式本身在当前环境中求值；函数体会在一个新的局部帧中执行。这个新局部帧的父帧通常是该函数定义时所在的环境。
Global frame（全局帧）包含两个绑定：
	mul -> 指向乘法函数func mul(...)
	square -> 指向函数对象func square(square) 
f1: square（局部帧）绑定关系：
	形参square被绑定到了实参4。这意味着在f1中，square不再是那个函数，而是数字4。
~~~

# Python特性

## `Docstrings`文档字符串

> `Docstring` 是写在模块、函数、类、方法内部的第一条语句位置的字符串，用来说明“这是干什么的”。
>
> 用三引号（`"""`或 `'''`）括起来，不是普通注释（#）。

## `Doctests`

>  `Doctest`是写在`docstring`里的交互式Python示例
>
>  `>>>`后面是Python交互式代码，可以是表达式，也可以是赋值等语句。
>
>  下一行写期望输出，Python会自动比对输出是否一致。如果某一行交互式代码本身没有显示输出，比如赋值语句，那么下面就不需要写期望输出。

# 复合语句—Compound Statements

> 复合语句是由其他语句（简单语句或复合语句）组成的语句，它会以某种方式控制/影响内部语句的执行。

![局部截取_20260705_195219](../../images/局部截取_20260705_195219.png)

~~~
Header（头部）：每个子句的开头部分（通常以关键字 + 冒号结尾）。
	头部的“关键字”决定了这条语句的类型。比如：
		以def开头 → 函数定义语句；
		以if开头 → 条件判断语句；
		以while开头 → 循环语句。
Clause（子句）：复合语句的基本组成单元。
Suite（套件/语句块）：跟在头部后面、被头部“控制”的一组语句（通常是缩进的代码块）。
	头部里的逻辑（比如if后面的条件、def后面的函数名和参数）决定了什么时候执行、怎么执行后面的Suite。
Separating header（分隔头部）：用于分隔多个子句（比如 elif、else）。
~~~

# 条件语句—Conditional Statements

![局部截取_20260705_202007](../../images/局部截取_20260705_202007.png)

~~~
if执行步骤:
	1.先评估当前子句的“条件表达式”。
	2.如果条件为真，执行该子句的suite，并跳过后续所有子句。
		
规则：
	必须以if开头，不能单独写elif或else。
	可以有0个或多个elif。
	可以有0个或1个else。
	
布尔上下文：程序中那些“只关心真假，不关心具体值”的执行场景。
Python中在布尔上下文中会被视为False的值如下表，除了表中那些假值，其他所有东西在布尔上下文中都被视为True。
~~~

|  类型  |         假值示例          |              说明              |
| :----: | :-----------------------: | :----------------------------: |
| 布尔值 |          `False`          |           本身就是假           |
|  数字  |        `0`, `0.0`         |        任何数值类型的零        |
| 字符串 |     `''`（空字符串）      |       长度为 0 的字符串        |
| 空容器 | `[]`, `()`, `{}`, `set()` | 空列表、空元组、空字典、空集合 |
| 特殊值 |          `None`           |       表示“无”或“未赋值”       |

# 循环语句—While Statements

![局部截取_20260705_204838](../../images/局部截取_20260705_204838.png)

~~~
while执行规则：
	1.评估头部表达式。
	2.如果是真值，执行整个套件，然后回到第一步。一旦某次头部表达式评估为假，解释器就会跳出循环，继续执行while语句后面的代码。
~~~

# 问题

~~~powershell
(base) PS D:\Study\AI-Learning> cd D:\Study\AI-Learning\CS61A\Lecture Notes\03_Control
Set-Location : A positional parameter cannot be found that accepts argument 'Notes\03_Control'.
At line:1 char:1
+ cd D:\Study\AI-Learning\CS61A\Lecture Notes\03_Control
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Set-Location], ParameterBindingException
    + FullyQualifiedErrorId : PositionalParameterNotFound,Microsoft.PowerShell.Commands.SetLocationCommand
~~~

解决：

​	路径中存在空格时，必须加引号，否则会把Lecture和Notes\03_Control当成两个参数。

~~~powershell
# 1.加双引号
cd "D:\Study\AI-Learning\CS61A\Lecture Notes\03_Control"
# 2.加单引号
cd 'D:\Study\AI-Learning\CS61A\Lecture Notes\03_Control'
~~~





