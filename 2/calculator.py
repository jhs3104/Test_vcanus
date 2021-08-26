class calculator():
    num = 0

    def add(self, n):
        self.num = self.num + n
        return self

    def subtract(self, n):
        self.num = self.num - n
        return self

    def out(self):
        return self.num


if __name__ == '__main__':
    result = calculator().add(4).add(5).subtract(3).out()
    print(result)
