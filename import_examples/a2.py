from b import g, var_b

var_a = 1
var_a_new = 100


def f(x):
    return x*x


print(f(var_a))
print(g(var_b))


print(f"my name is {__name__}")