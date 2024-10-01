from math import sqrt

class Vec2:

    def __init__(self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
        except (ValueError, TypeError):
            raise ValueError("vector components must be "
                             "integers or floats")

    def length(self):
        return sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return f"Vector 2D (x: {self.x}, y: {self.y})"

    def __add__(self, other):
        if type(other) == Vec2:
            x = self.x + other.x
            y = self.y + other.y
            return Vec2(x,y)
        else:
            raise ValueError("vector addition requires two vectors")

    def __mul__(self, other):
        # Dot product
        if type(other) == Vec2:
            return self.x*other.x + self.y*other.y

        # Scalar multiplication (not to be confused with scalar product)
        else:
            try:
                k = float(other)
            except ValueError:
                raise ValueError("scalar multiplication requires "
                                 "an integer or float")
            
            return Vec2(k*self.x, k*self.y)


def quadsolve(a,b,c,y):
    """ Solve a*x**2 + b*x + c = y for x """
    c = c-y
    d = b**2 - 4*a*c
    roots = []

    if d > 0:
        r1 = (-b + sqrt(d))/(2*a)
        r2 = (-b - sqrt(d))/(2*a)
        roots.append(r1)
        roots.append(r2)

    elif d == 0:
        r = -b/(2*a)
        roots.append(r)

    # else no real roots

    return roots

def max2(seq):
    """ Finds the largest element in sequence seq
        and returns the value along with its location (index)
        in the sequence. 
        
        If the sequence contains duplicates the only 
        the first occurence is reported. """
    try:
        m = seq[0]
        idx = 0
    except IndexError:
        raise ValueError("max2() arg is an empty sequence")

    for i, s in enumerate(seq[1:], start=1):
        if s > m:
            m = s
            idx = i

    return (idx, m)

if __name__ == "__main__":
    a = Vec2(1,2)
    # a = Vec2(1, "two" )
    b = Vec2(3,4)

    print(a)
    print("|b|", b.length())


    print("a+b", a+b)
    #print("a+2", a+2)

    print("a dot b", a*b)
    print("a * 2", a*2)

    print(quadsolve(2,0,0,8))
    print(quadsolve(2,4,-4,0))

    print(max2([1,2]))
    print(max2([1,2,3,3,4,4]))
