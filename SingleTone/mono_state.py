class MonoState(object):
    '''
    diffrent objects with shared state
    '''
    shared_state="old"
    shared_state_plus=["old"]
    def __init__(self, name):
        self.name=name


obj1=MonoState("obj1")
obj2=MonoState("obj2")

print( "obj1.name: ", obj1.name,\
       "obj2.name: ", obj2.name,\
       "obj1.shared_state: ", obj1.shared_state,\
       "obj2.shared_state: ", obj2.shared_state)

obj1.shared_state="New"
print(obj1.shared_state)
print(obj2.shared_state)
MonoState.shared_state="changed"
print(obj2.shared_state)
print(obj1.shared_state)
obj3=MonoState("obj3")
print(obj3.shared_state)

print("_"*10)

print(obj1.shared_state_plus)
obj1.shared_state_plus[0]="New"
print(obj1.shared_state_plus)
print(obj2.shared_state_plus)
MonoState.shared_state_plus[0]="changed"
print(obj2.shared_state_plus)
print(obj1.shared_state_plus)
obj3=MonoState("obj3")
print(obj3.shared_state_plus)

print("_"*10)

print(obj1.shared_state_plus)
obj1.shared_state_plus=["New"]
print(obj1.shared_state_plus)
print(obj2.shared_state_plus)
MonoState.shared_state_plus[0]="changed"
print(obj2.shared_state_plus)
print(obj1.shared_state_plus)
obj3=MonoState("obj3")
print(obj3.shared_state_plus)
