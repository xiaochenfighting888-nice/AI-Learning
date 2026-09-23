class Ratio:
    def __init__(self, n, d):
        """初始化有理数，n 为分子，d 为分母"""
        self.numer = n
        self.denom = d

    def __repr__(self):
        """返回对象的 Python 表示形式，方便调试和重新创建对象"""
        return "Ratio({0}, {1})".format(self.numer, self.denom)

    def __str__(self):
        """返回用户可读的分数形式字符串"""
        return "{0}/{1}".format(self.numer, self.denom)

    def __add__(self, other):
        """实现有理数与整数、其他有理数、浮点数之间的加法"""
        if isinstance(other, int):
            n = self.numer + self.denom * other
            d = self.denom

        elif isinstance(other, Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom

        elif isinstance(other, float):
            return float(self) + other

        g = gcd(n, d)
        return Ratio(n // g, d // g)

    __radd__ = __add__

    def __float__(self):
        """将有理数转换为浮点数"""
        return self.numer / self.denom


def gcd(n, d):
    """计算两个整数的最大公约数"""
    while n != d:
        n, d = min(n, d), abs(n - d)
    return n
