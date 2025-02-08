# write a class "calculator" capable of finding square. cube and square root of a number

class Calculator():
    def __init__(self, n):
        self.n = n

# this is square function
    def square(self):
        print(f"square is {self.n * self.n}")


# this is cube function
    def cube(self):
        print(f"cube is {self.n * self.n * self.n}")


# this is square-root function
    def squareRoot(self):
        print(f"squareRoot is {self.n ** 1/2}")

no = Calculator(5)
no.square()
no.cube()
no.squareRoot()