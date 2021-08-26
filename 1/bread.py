import json

# breadJson
breadJson = [
    {
        "breadType": "cream",
        "recipe": {
            "flour": 100,
            "water": 100,
            "cream": 200
        }
    },
    {
        "breadType": "sugar",
        "recipe": {
            "flour": 100,
            "water": 50,
            "sugar": 200
        }
    },
    {
        "breadType": "butter",
        "recipe": {
            "flour": 100,
            "water": 100,
            "butter": 50
        }
    }
]


# 추상 클래스, 메소스 생성
class bread():
    CREAM = 0
    SUGAR = 1
    BUTTER = 2

    def print_bread(self):
        pass


# creambread 클래스
class creambread(bread):
    def print_bread(self, data):
        data = json.loads(data)
        for key, value in data.items():
            if key == "breadType":
                print(key, ":", value)
            else:
                for keys, values in data['recipe'].items():
                    print(keys, ":", values)
                break


# sugarbread 클래스
class sugarbread(bread):
    def print_bread(self, data):
        data = json.loads(data)
        for key, value in data.items():
            if key == "breadType":
                print(key, ":", value)
            else:
                for keys, values in data['recipe'].items():
                    print(keys, ":", values)
                break


# butterbread 클래스
class butterbread(bread):
    def print_bread(self, data):
        data = json.loads(data)
        for key, value in data.items():
            if key == "breadType":
                print(key, ":", value)
            else:
                for keys, values in data['recipe'].items():
                    print(keys, ":", values)
                break


# 팩토리 생성
class breadFactory():
    def getbread(self, breadType, data):
        if breadType == bread.CREAM:
            return creambread().print_bread(data)
        elif breadType == bread.SUGAR:
            return sugarbread().print_bread(data)
        elif breadType == bread.BUTTER:
            return butterbread().print_bread(data)


if __name__ == '__main__':
    breadJsondata = breadFactory()  # 팩토리 객체 생성
    for typebread in breadJson:  # Json을 순회하면서 Type확인 후 맞는 클래스 호출
        if typebread["breadType"] == "cream":
            data = json.dumps(typebread)
            breadJsondata.getbread(bread.CREAM, data)

        elif typebread["breadType"] == "sugar":
            data = json.dumps(typebread)
            breadJsondata.getbread(bread.SUGAR, data)
        else:
            data = json.dumps(typebread)
            breadJsondata.getbread(bread.BUTTER, data)
