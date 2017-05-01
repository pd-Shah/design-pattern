class LazyInstantiation(object):
    _allocate=True
    def __new__(cls, *args):
        if not hasattr(cls, "_instance"):
            cls._instance=object.__new__(cls)
        return cls._instance

    def __init__(self, name=None):
        if LazyInstantiation._allocate:
            LazyInstantiation._allocate=False
            print("allocate resources...")
            self.name=name
        else:
            print("SingleTone without allocating.")

x=LazyInstantiation("pd")
y=LazyInstantiation()
print(id(x)==id(y))
print(y.name)
print("_"*10)
