print("IMPORTED MODULE")

from .e import var_e

print(f"THIS IS MY var_e={var_e}")

x = 15

__all__ = [
    "var_e"
]