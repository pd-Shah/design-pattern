class Implementation1:
    def f(self):
        print("Implementation.f()")
    def g(self):
        print("Implementation.g()")
    def h(self):
        print("Implementation.h()")

class Implementation2:
    def method1(self):
        print("method1")


class Proxy:
    def __init__(self):
        self._implementation1 = Implementation1()
        self._implementation2=  Implementation2()
    # Pass method calls to the implementation:
    def f(self): self._implementation1.f()
    def g(self): self._implementation1.g()
    def h(self): self._implementation1.h()
    def method1(self): self._implementation2.method1()
