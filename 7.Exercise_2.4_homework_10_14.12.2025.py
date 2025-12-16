class A:
    def who_am_i(self):
        print("A")

class B(A):
    def who_am_i(self):
        print("B")
class C(A):
    def who_am_i(self):
        print("C")

class D(B, C): pass

d = D()
d.who_am_i()
print(D.__mro__)
