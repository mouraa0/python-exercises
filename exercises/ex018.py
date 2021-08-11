import math
a = float(input('Ângulo: '))
sin = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print(f'sin({a}°) = {sin:.2f}\ncos({a}°) = {cos:.2f}\ntan({a}°) = {tan:.2f}')