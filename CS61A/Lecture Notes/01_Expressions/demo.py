# Expressions demo
from operator import add, mul


def main():
    # 中缀表达式：运算符在操作数之间,需要明白运算符的优先级
    print(2 + 2 * 3 // 4)
    # 函数调用表达式:无需了解运算符的优先级,直接计算
    print(add(2, 2))
    # 函数调用形式的嵌入表达式:一个表达式嵌套在另一个表达式中
    # 子表达式完全求值成“值”,就可进行下一步计算
    # add(3,4)先计算成7，然后执行mul(7,5)
    print(mul(add(3, 4), 5))

if __name__ == "__main__":
    main()
