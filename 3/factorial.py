def factorial(num):
    if num == 1:  # 재귀함수 탈출 조건
        return 1
    return num * factorial(num - 1)  # 재귀함수 호출


if __name__ == '__main__':
    result = factorial(4)
    print(result)
