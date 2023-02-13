class Firstclass:
    a = 1
    b = 2
    name = "swati"

    # constructor
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "this is my first class"

    def sayHello(self):
        # print("hello, world!")
        print(f'hello,{self.name}')


obj = Firstclass("swati")
print(obj)
obj.sayHello()

print(obj.name)
