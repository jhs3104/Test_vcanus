def flow(num, acc):
    if num == 1:
        return acc
    return flow(num - 1, acc * num)


def factorial(num):
    return flow(num, 1)


if __name__ == '__main__':
    result = factorial(5)
    print(result)
