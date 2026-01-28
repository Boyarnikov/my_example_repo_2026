from b import g, var_b
import directory.d as this_d

import directory
import module_directory

from module_directory import *

var_a = 1
var_a_new = 100


def f(x):
    return x*x


print(f(var_a))
print(g(var_b))
print(this_d.var_d)


print(dir(module_directory))
print(module_directory.var_e)
print(module_directory.x)
print(var_e)
#print(x)