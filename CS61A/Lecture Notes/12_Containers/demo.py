def index(keys, values, match):
    """将每个 k 映射到 values 中所有满足 match(key, value) 的值"""

    return {k: [v for v in values if match(k, v)] for k in keys}


if __name__ == "__main__":
    print(
        index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
    )  # {7: [35, 42, 49], 9: [36, 45], 11: [33, 44]}
