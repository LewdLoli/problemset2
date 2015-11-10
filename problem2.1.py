poly = (0.0, 0.0, 5.0, 9.3, 7.0)
x = -13

def evauluate_poly(poly,  x):
    number = 0
    for i in range (0, len(poly)):
       number += poly[i] * x ** i
    return number

print evauluate_poly(poly, x)
