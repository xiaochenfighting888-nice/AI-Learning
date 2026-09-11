def remove(n, digit):
    """从非负整数 n 中删除所有等于 digit 的数字，并返回剩余数字组成的新整数"""
    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            # kept = kept + last * 10**digits
            kept = last * pow(10, digits) + kept
            digits = digits + 1
    return kept


if __name__ == "__main__":
    print(remove(45321231, 3))  # 452121
