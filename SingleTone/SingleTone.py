class SingleTone(object):
    def __new__(cls, *args):
        if not hasattr(cls, "_instance"):
            cls._instance=object.__new__(cls)
        return cls._instance
    def __init__(self, name):
        self.name=name

x=SingleTone("obj1")
y=SingleTone("obj2")

print("id(x) =? id(y): ", id(x) == id(y))
print("x.name: %s"%x.name, "y.name: %s"%y.name)
x.family="family"
print("y.family: ", y.family)
print("x: ", x)
