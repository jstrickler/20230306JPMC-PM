#!/usr/bin/env python

print('26\u00B0')  # <1>
print('26\N{DEGREE SIGN}')  # <2>
print(r'26\u00B0\n')  # <3>
print()

print('we spent \u20ac1.23M for an original C\u00e9zanne') # <4>
print("Romance in F\u266F Major")
print()

data = ['\U0001F95A', '\U0001F414']  # <5>
print("unsorted:", data)
print("sorted:", sorted(data))

print("\U0001F92F")

#  <= FFFF    \uxxxx    pad with 0 as needed  \u00B0
#  > FFFF     \Uxxxxxxxx                      \U0001F95A

print("\U0001f608")