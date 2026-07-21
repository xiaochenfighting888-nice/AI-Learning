# 高阶函数与环境图

> 环境图主要用于描述Python函数执行过程中的环境变化，包括函数调用、变量绑定以及函数对象与父环境之间的关系。

![局部截取_20260709_213740](../../images/局部截取_20260709_213740.png)

~~~
调用用户定义函数：
	1.创建一个新的帧。
	2.将形式参数与实际参数绑定。
	3.执行函数体，根据函数逻辑计算返回值。
        例如：return f(f(x))
        表示函数组合：先计算f(x)，再将结果作为参数传递给外层的f。
~~~

# 嵌套定义的环境图

> return会结束当前函数调用，并将计算结果返回给调用者所在的环境。
>
> 函数的父级设置为该函数创建时的当前帧，adder函数的父级环境是创建它时所在的make_adder调用帧。
>
> 局部帧都有一个父级帧。
>
> 知道调用的哪个函数，就会正确画下它的帧。

![局部截取_20260709_232119](../../images/局部截取_20260709_232119.png)

~~~
第一阶段：第1-5行（定义函数，不执行内部逻辑）
	动作：Python解释器读取代码，创建函数对象，但不执行函数体。
	环境变化：在Global frame（全局环境）中，创建了func make_adder(n)，将其和名字make_adder绑定在一起。虽然make_adder内部定义了adder，但在这一步，adder还没有被创建。只有当make_adder被调用时，内部的def adder(k)才会执行。
第二阶段：add_three = make_adder(3)
	调用make_adder(3)，Python创建一个新的环境帧f1。
	它的parent（父环境）指向Global（全局环境）。
	在f1中，参数n被绑定为值3。
	进入make_adder内部，执行def adder(k)。此时才真正创建了func adder(k)。
    这个adder函数的[parent=f1]。这意味着，虽然adder是在make_adder里定义的，但它的“老家”指向了f1（而不是Global）。这样它就永久保留了访问f1中n的能力。
	执行到最后一行return adder。返回的是刚刚创建好的func adder(k)（它带着f1的引用）。
	回到Global：表达式make_adder(3)求值完成，结果是func adder。全局变量add_three被绑定到这个返回的函数对象上。
第三阶段：add_three(4)
	调用add_three(4)，即调用之前返回的adder(4)。创建新的环境帧f2。
	它的parent指向f1（因为adder是在f1中定义的）。
	在f2中，参数k被绑定为值4。
	执行return k + n。
    找k：在当前的f2中找到k = 4。
    找n：f2里没有n，于是顺着parent指针向上查找，找到了f1中的n = 3。
    计算结果：4 + 3 = 7。
~~~

# 绘制环境图

![局部截取_20260711_120146](../../images/局部截取_20260711_120146.png)

> 当定义一个函数时：
>
> ​	创建一个函数对象：`func <name>(<formal parameters>) [parent=<parent>]`
>
> ​	函数对象的parent指向当前正在执行的环境帧（也就是定义它时所在的那个帧）。这里父级帧的名字不写make_adder，是因为可能有多个不同的被称为make_adder的框架，应该用唯一的标签。
>
> ​	在当前帧中，将函数名<name>和函数对象捆绑在一起。

> 当调用函数的时候：
>
> ​	创建一个新的局部帧，以调用函数的名称为标题的局部帧。
>
> ​	复制函数的父环境到新帧：`[parent=<label>]`。
>
> ​	在新的帧中将形参<formal parameters>和参数捆绑在一起。
>
> ​	在新的环境中执行函数体。
>
> ​	在该环境沿着父级一直追溯到全局帧，首次找到该名称，则就是所需要查找的名字。

# 局部名称—Local Names

> 函数的形式参数具有局部范围。
>
> 局部名称在其他不是嵌套函数的函数中是看不见的。

![局部截取_20260714_213633](../../images/局部截取_20260714_213633.png)

> Top-level function（顶层函数）：指的是没有被定义在另一个函数内部的函数。也就是说，它直接定义在全局作用域中（即没有 `def`套 `def`的情况）。
>
> 当你调用一个顶层函数时，程序会构建一个执行环境。这个环境的构成很简单：最前面是一个局部框架（专门给这个函数本次调用用），紧接着后面就是全局框架。

# 函数组合 — Function Composition

> 将多个函数组合成一个新的函数。
>
> 例如： compose(f, g)(x) 等价于：f(g(x)) 
>
> 执行顺序：
>
> ​	1.先执行g(x)。
>
> ​	2.再将结果传入f。

![局部截取_20260714_222446](../../images/局部截取_20260714_222446.png)

# lambda表达式

> 赋值语句将一个值或者函数绑定到名字上，`lambda`可以用相同的语法，一条赋值语句，将一个函数绑定到一个名字上。

![局部截取_20260720_222927](./../../images/局部截取_20260720_222927.png)

> `square = x * x`是一个表达式，求值结果为数字100。
>
> `lambda x: x * x`是一个表达式，求值结果是一个函数对象。
>
> `lambda`表达式没有`return`关键字，冒号后面的表达式的计算结果会自动作为返回值。
>
> `lambda`不能包含多条语句，不能写普通的`if/else`代码块和循环语句，只能包含一个表达式。
>
> 把一个匿名函数直接赋值给变量`square`，然后像普通函数一样调用它`square(4)`，结果依然是`16`。

# lambda表达式 VS def定义函数

![局部截取_20260721_175849](./../../images/局部截取_20260721_175849.png)

> 两者都创建了一个具有相同定义域（domain）、值域（range）和行为（behavior）的函数。
>
> 这两个函数的父环境都是它们被定义时所在的环境帧。
>
> 两者都将该函数绑定到了名字`square`上。
>
> 只有使用`def`定义的函数，在创建时会自动拥有一个与函数名相同的内部名称。
>
> ​	内部名称是函数对象在创建时自带的内部属性，写在函数定义里，不会因为变量名的变化而改变。即函数的\_\_name\_\_属性。

~~~powershell
PS D:\ai-learning\cs61a\lecture notes\05_environments> python -i demo1.py
>>> square1
<function <lambda> at 0x0000026291C4B7F0>
>>> square2
<function square2 at 0x000002629215BC10>
>>> square1.__name__
'<lambda>'
>>> square2.__name__
'square2'
~~~

# 函数柯里化 — Function Currying

> Currying是把一个“接收多个参数的函数”，转换成一系列“每次只接收一个参数的函数“的技术。

~~~powershell
PS D:\ai-learning\cs61a\lecture notes\05_environments> python -i demo2.py
>>> from operator import add
>>> m = curry(add)
>>> m(2)(3)
5
>>> add_three = m(3)
>>> add_three(2) 
5
>>> add_three(2026)
2029
>>> curry = lambda f: lambda x: lambda y: f(x, y)
>>> m = curry(add)
>>> m(2)(3)
5
~~~

