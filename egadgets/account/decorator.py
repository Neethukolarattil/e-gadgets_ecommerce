#Decorators

# changing functionality without changing its functional properties



def dec(fn):
    def inner(a,b):
        if a>b:
            return fn(a,b)
        else:
            return fn(b,a)
    return inner
@dec
def sub(a,b):
    print(a-b)

@dec
def div(a,b):
    print(a/b)

sub(100,20)
div(100,20)