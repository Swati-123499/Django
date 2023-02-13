class Mathclass:

    def sum(self, a, b):
        return a+b

    def sub(self, a, b):
        return a-b

    def mul(self, a, b):
        return a*b

    def div(self, a, b):
        return a/b

    def mod(self, a, b):
        return a % b


# self is a keyword

class Expression(Mathclass):

    def lhs(self, a, b):
        return self.mul(
            self.sum(a, b),
            self.sum(a, b)
        )

    def rhs(self, a, b):
        return self.sum(
            self.sum(
                self.mul(a, a),
                self.mul(b, b)
            ),
            self.sum(
                self.mul(a, b),
                self.mul(a, b)
            )
        )


obj = Expression()

print(obj.rhs(2, 3))

print(obj.lhs(2, 3))


"""
obj = Mathclass()
print(obj.sum(10, 63))
print(obj.sub(10, 63))
print(obj.mul(10, 63))
print(obj.div(10, 63))
print(obj.mod(10, 63))
"""
