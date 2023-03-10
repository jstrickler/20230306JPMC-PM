from math import pi as PI

def circle_area(diameter):
    radius = diameter / 2
    area = PI * radius ** 2
    return area

def rectangle_area(length, width):
    return length * width

def square_area(length):
    return length ** 2

if __name__ == '__main__':
    c = circle_area(10)
    r = rectangle_area(5, 10)
    s = square_area(5)
    print(c, r, s)