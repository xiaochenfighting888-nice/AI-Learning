def split(n):
    """把数字拆成“去掉末位的部分”和“末位数字”"""
    return n // 10, n % 10


def sum_digits(n):
    """计算一个非负整数的各位数字之和"""
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last


def luhn_sum(n):
    """
    计算非负整数 n 的 Luhn 校验和，最右边一位不翻倍
    从右往左，交替按“保持原值、翻倍后求数字和”处理各位，再累加
    """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last


def luhn_sum_double(n):
    """
    辅助计算 Luhn 校验和，最右边一位需要翻倍
    从右往左，交替按“翻倍后求数字和、保持原值”处理各位，再累加
    """
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit


if __name__ == "__main__":
    print(sum_digits(2026))  # 10
    print(luhn_sum(5105105105105100))  # 20
