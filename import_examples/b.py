import c


var_b = 2
var_b_new = 200


def g(x):
    return x*x*x


print("finish import from b!")


print(f"my name (from b) is {__name__}")


if __name__ == "__main__":
    print("МЕНЯ ЗАПУСТИЛИ КАК ФАЙЛ")

if __name__ == "b":
    print("МЕНЯ ЗАПУСТИЛИ КАК МОДУЛЬ b")