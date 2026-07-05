"""
利用命令行python -i demo2.py执行
进入交互模式，用于检查和调试程序中的变量与函数
"""

# python -i demo2.py：先运行demo2.py，然后自动进入Python交互式环境，继续“现场调试”


def divide_exact(n, d):
    """返回n除以d的商和余数的函数"""
    return n // d, n % d


quotient, remainder = divide_exact(2026, 10)
