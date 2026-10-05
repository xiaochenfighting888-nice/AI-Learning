# `SQL` 多表连接

`FROM` 后面可以同时写多个表：

```sql
select *
from parents, dogs;
```

假设 `parents` 表包含：

|   parent   |  child   |
| :--------: | :------: |
|  abraham   |  barack  |
|  abraham   | clinton  |
|   delano   | herbert  |
|  fillmore  | abraham  |
|  fillmore  |  delano  |
|  fillmore  |  grover  |
| eisenhower | fillmore |

而 `dogs` 表包含：

|    name    |  fur  |
| :--------: | :---: |
|  abraham   | long  |
|   barack   | short |
|  clinton   | long  |
|   delano   | long  |
| eisenhower | short |
|  fillmore  | curly |
|   grover   | short |
|  herbert   | curly |

## 笛卡尔积

> 笛卡尔积是指两张表没有任何连接条件时，将第一张表的每一行与第二张表的每一行进行两两组合，结果行数 = 表A行数 × 表B行数。

从逻辑上可以把：

```sql
from parents, dogs
```

理解为两张表的笛卡尔积。

假设：

```
parents 有 7 行
dogs 有 8 行
```

那么逻辑上共有：

```
7 × 8 = 56
```

种可能的行组合。

例如 `parents` 第一行：

```
abraham | barack
```

会分别与 `dogs` 的每一行组合：

```
abraham | barack | abraham    | long
abraham | barack | barack     | short
abraham | barack | clinton    | long
abraham | barack | delano     | long
abraham | barack | eisenhower | short
abraham | barack | fillmore   | curly
...
```

所以：

```sql
select *
from parents, dogs;
```

并不是直接“根据关系连接两个表”。

从逻辑上可以理解为：

```
	所有可能的行组合
         ↓
通过 WHERE 筛选需要的组合
```

## 表连接

表连接（Join）的核心思想是：

```
  先组合两个表中的行
	    ↓
  再根据某个相关条件
	    ↓
只留下能够对应起来的行
```

例如：

```sql
select *
from parents, dogs
where child = name;
```

表示：只保留 `parents.child` 和 `dogs.name` 相同的行。

`SQL` 不限制只能连接两个表。

## 多个 WHERE 条件

连接之后还可以继续增加筛选条件。

例如：

```sql
select *
from parents, dogs
where child = name
  and fur = 'curly';
```

这里有两个条件：

```
child = name
```

负责把两个表中对应的对象连接起来。

```
fur = 'curly'
```

负责进一步只保留毛发为 `curly` 的对象。

## 多表查询的逻辑顺序

对于：

```sql
select parent
from parents, dogs
where child = name
  and fur = 'curly';
```

可以按照下面的顺序理解：

```
		   FROM
			↓
找到 parents 和 dogs 两个输入表

	笛卡尔积
	   ↓
产生所有可能的行组合

WHERE child = name
		↓
留下两个表中能够对应的行

AND fur = 'curly'
		↓
	 继续过滤

 SELECT parent
  	   ↓
  只输出需要的列
```

## 表别名

给表起短名称：

```sql
select p.parent
from parents as p, dogs as d
where p.child = d.name
  and d.fur = 'curly';
```

这里：

```
p → parents
d → dogs
```

于是：

```sql
p.child
```

就是：

```sql
parents.child
```

而：

```sql
d.name
```

就是：

```sql
dogs.name
```

## JOIN

下面这种写法：

```sql
from parents, dogs
where child = name
```

属于用 `WHERE` 描述连接条件的写法。

也可以写成更明确的：

```sql
select p.parent
from parents as p
join dogs as d
  on p.child = d.name
where d.fur = 'curly';
```

这里：

```sql
on p.child = d.name
```

专门负责说明：

```
两个表如何连接
```

而：

```sql
where d.fur = 'curly'
```

专门负责连接后的进一步筛选。

## 自连接

> 自连接（self join）指的是：同一个表在一次查询中被使用多次，并把它当成多个独立的输入表进行连接。

例如：

```sql
from parents as a, parents as b
```

虽然：

```text
a
b
```

都来自同一个 `parents` 表，但在当前查询中可以把它们理解成两份独立的表：

```text
parents → a
parents → b
```

这样就可以把 `parents` 表中的一行与同一个表中的另一行进行比较。

## 点表达式

多个表可能拥有相同的列名。

例如：

```sql
from parents as a, parents as b
```

两边都有：

```text
parent
child
```

如果直接写：

```sql
child
```

`SQL` 无法明确知道指的是哪一个表中的 `child`。

因此使用：

```sql
a.child
b.child
```

这种形式。

一般形式：

```text
表名或别名.列名
```

例如：

```sql
a.parent
```

表示：

```text
a 表中的 parent 列
```

这种写法可以消除多个表之间的列名歧义。

# `SQL` 表达式

> `SQL` 中很多位置都可以使用表达式（expression），而不仅仅是简单的列名。

基本查询结构：

```sql
SELECT 表达式 AS 列名
FROM 表
WHERE 条件
ORDER BY 表达式
```

表达式中还可以包含：

```text
列名
常量
算术运算
比较运算
逻辑运算
函数调用
```

## 数值表达式

`SQL` 支持常见的算术运算：

```text
+   加法
-   减法
*   乘法
/   除法
%   取余
```

例如：

```sql
select x + 1
from numbers;
```

对于输入表的每一行，都会取当前行中的 `x` 计算：

```text
x + 1
```

这里的普通标量表达式会针对当前输入行进行求值。

除了减法：

```sql
a - b
```

`-` 还可以直接作用于一个值：

```sql
-x
```

表示取相反数。

例如：

```sql
select -5;
```

得到：

```text
-5
```

## 数值函数

表达式中还可以调用函数。

常见函数包括：

```sql
abs(x)
```

求绝对值。

例如：

```sql
select abs(-5);
```

得到：

```text
5
```

---

```sql
round(x)
```

进行四舍五入。

例如：

```sql
select round(3.6);
```

得到：

```text
4.0
```

还可以写成：

```sql
round(x, n)
```

保留指定的小数位数。

## 比较表达式

`SQL` 支持：

```text
<    小于
<=   小于等于
>    大于
>=   大于等于
=    等于
!=   不等于
<>   不等于
```

注意 `SQL` 判断相等使用：

```sql
=
```

而不是 Python 中的：

```python
==
```

例如：

```sql
where age >= 18
```

表示只保留：

```text
age 大于等于 18
```

的行。

## 逻辑表达式

多个条件可以使用：

```sql
and
or
not
```

组合。

例如：

```sql
where age >= 18
  and age < 60
```

表示：

```text
age >= 18 并且 age < 60
```

两个条件都成立时才保留这一行。

---

例如：

```sql
where fur = 'curly'
   or fur = 'long'
```

表示：

```text
curly 或 long
```

满足任意一个即可。

---

`not` 用于取反：

```sql
where not age < 18
```

表示：

```text
不是 age < 18
```

也就是筛选成年数据。

## 字符串表达式

`SQL` 也可以对字符串进行处理。

字符串可以：

```text
连接
截取
查找
组合
```

### 字符串连接

`SQLite` 使用：

```sql
||
```

连接两个字符串。

例如：

```sql
select 'hello,' || ' world';
```

得到：

```text
hello, world
```

### 列值之间的连接

假设表中：

```text
first = hello
second = world
```

可以写：

```sql
select first || second
from words;
```

把当前行中的两个字符串连接起来。

也可以加入固定字符串：

```sql
select first || ', ' || second
from words;
```

得到：

```text
hello, world
```

### `substr` 截取字符串

`SQLite` 中：

```sql
substr(string, start, length)
```

用于从字符串中截取一部分。

例如：

```sql
substr('hello', 2, 3)
```

从第 2 个字符开始，取 3 个字符：

```text
ell
```

需要注意：`SQLite` 的字符串位置从 `1` 开始，而不是像 Python 一样从 `0` 开始。

例如：

```text
hello
12345
```

所以：

```sql
substr('hello', 1, 1)
```

得到：

```text
h
```

### instr 查找字符串位置

`SQLite` 中：

```sql
instr(string, substring)
```

用于查找一个字符串第一次出现的位置。

例如：

```sql
instr('hello, world', ' ')
```

空格出现在第：

```text
7
```

个位置，所以结果为：

```text
7
```

同样使用从 `1` 开始的位置编号。

### `instr` 与 `substr` 组合

假设：

```sql
create table phrase as
select 'hello, world' as s;
```

执行：

```sql
select substr(s, 4, 2)
from phrase;
```

字符串：

```text
h e l l o ,   w o r l d
1 2 3 4 5 6 7 8 9 ...
```

从位置 `4` 开始取两个字符：

```text
lo
```

再看：

```sql
instr(s, ' ')
```

得到空格位置：

```text
7
```

所以：

```sql
instr(s, ' ') + 1
```

得到：

```text
8
```

也就是：

```text
w
```

所在的位置。

因此：

```sql
substr(s, instr(s, ' ') + 1, 1)
```

得到：

```text
w
```

组合起来：

```sql
select substr(s, 4, 2)
       || substr(s, instr(s, ' ') + 1, 1)
from phrase;
```

得到：

```text
low
```

### 字符串表示结构化数据

字符串也可以强行保存一些具有内部结构的数据。

例如：

```sql
create table lists as
select 'one' as car,
       'two,three,four' as cdr;
```

这里：

```text
two,three,four
```

实际上用一个字符串模拟了：

```text
多个数据组成的列表
```

如果想取第一个元素：

```text
two
```

可以先查找第一个逗号：

```sql
instr(cdr, ',')
```

然后：

```sql
substr(cdr, 1, instr(cdr, ',') - 1)
```

就可以取得：

```text
two
```

虽然这种方式可以实现：

```text
'two,three,four'
```

表示多个数据，

但通常并不是好的数据库设计。

原因是：

```text
每次读取数据
都要进行字符串查找和切割
```

而数据库本身已经提供了：

```text
行
列
表
关系
```

来表示结构化数据。

所以更合理的方式通常是：

```text
不同的数据 → 放到不同列或不同记录中
```

而不是：

```text
把很多数据塞进一个字符串 → 再手动解析
```

