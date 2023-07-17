class A:
    def set_number(self):
        self.x = 20
a = A()
a.set_number()
b = A()
print(a.__dict__)
print(b.__dict__)
