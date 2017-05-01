class State:
    def __init__(self, cls):
        self.engine=cls()
        

    
class Implementation1():
    def f(self):
        print("Implementation1 -> f")
    def g(self):
        print("Implementation1 -> g")
    def h(self):
        print("Implementation1 -> h")

class Implementation2():
    def f(self):
        print("Implementation2 -> f")
    def g(self):
        print("Implementation2 -> g")
    def h(self):
        print("Implementation2 -> h")

def run(b):
    b.f()
    b.g()
    b.h()

b = State(Implementation1)
run(b.engine)

b = State(Implementation2)
run(b.engine)
