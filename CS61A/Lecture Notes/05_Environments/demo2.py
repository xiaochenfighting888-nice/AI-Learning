# 将接收两个参数的函数转换为两个连续接收一个参数的函数
# 例如：add(x,y)转换为：add(x)(y)


# curry(add)(2)(3)等价于：add(2,3)
def curry(f):
    def g(x):
        def h(y):
            return f(x, y)

        return h

    return g
