class AwesomeCal:
    def __init__(self, value):
        self.value = value
    def add(self,num):
        self.value += num
        return self.value
    def sub(self,num):
        self.value -= num
        return self.value
    def mul(self,num):
        self.value *= num
        return self.value
    def div(self,num):
        if (num==0):
            self.value=-9999
        else:
            self.value /= num
        return self.value
    def changeVal(self,num):
        self.value=num
        return self.value


a = AwesomeCal(100)
a.add(5)
print(a.value)     # 105
a.sub(10)
print(a.value)     # 95
a.changeVal(30)
a.mul(5) 
print(a.value)     # 150
a.div(0) 
print(a.value)