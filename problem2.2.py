poly = (-13.39, 0.0, 17.5, 3.0, 1.0)

def compute_deriv(poly):
    newPoly = list(poly)
    newPoly.pop(0)

    for i in range(0, len(newPoly)):
       newPoly[i] = newPoly[i] * (i + 1)

    poly = tuple(newPoly)
    return poly
print compute_deriv(poly)
