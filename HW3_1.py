class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def sub(self):
        return self.first - self.second
    def mul(self):
        return self.first * self.second
    def div(self):
        return self.first / self.second


class MoreCal(Calculator):
    def pow(self):
        return self.first**self.second
    def quotient(self):
        return self.first//self.second
    def mod(self):
        return  self.first%self.second

a= MoreCal(2,4)
print(a.add())
print(a.pow())
print(a.quotient())
print(a.mod())

b= MoreCal(5,3)
print(b.pow())
print(b.quotient())
print(b.mod())