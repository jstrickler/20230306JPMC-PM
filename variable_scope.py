x = 100   # global variable


def spam():
    animal = "wombat"  # local variable
    x = 42
    print(f"in spam() x: {x}")

spam()

print(f"(main) x: {x}")

