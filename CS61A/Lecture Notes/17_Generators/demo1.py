def countdown(n):
    """从 n 开始倒计时，并在最后产生 'blast off'"""
    if n > 0:
        yield n
        yield from countdown(n - 1)
    else:
        yield "blast off"


def prefixes(s):
    """依次产生字符串 s 的所有非空前缀"""
    if s:
        yield from prefixes(s[:-1])
        yield s


def substrings(s):
    """依次产生字符串 s 的所有非空子串"""
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])


if __name__ == "__main__":
    print(list(countdown(3)))
    print(list(prefixes("abc")))
    print(list(substrings("abc")))
