import sys
# from pkg.pkg import module
from alpha.mathlib import geometry

# look for geometry.py

# import venkat.spam

a = geometry.circle_area(99)
print(f"a: {a}")

b = geometry.square_area(14)
print(f"b: {b}")

# import search path
# 1. current folder
# 2. folders in PYTHONPATH
# 3. builtin folders (sys.prefix)
print(f"sys.prefix: {sys.prefix}")
print()
for path in sys.path:
    print(path)



