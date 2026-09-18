def make_withdraw_list(balance):
    """
    创建一个带余额状态的取款函数
    返回的函数可以修改并保存当前余额
    """
    b = [balance]

    def withdraw(amount):
        """尝试取款并返回剩余余额"""
        if amount > b[0]:
            return "余额不足"
        else:
            b[0] = b[0] - amount
            return b[0]

    return withdraw


if __name__ == "__main__":
    withdraw = make_withdraw_list(100)

    print(withdraw(25))
    print(withdraw(30))
    print(withdraw(60))
