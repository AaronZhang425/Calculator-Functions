from math import *


def quad_equation(a, b, c):

    try:
        radical = (b**2)-(4*a*c)
        sqroot = sqrt(radical)
        ans1 = str((-b - sqroot) / (2 * a))
        ans2 = str((-b + sqroot) / (2 * a))

        if ans1 == ans2:
            return 'x = ' + ans1
        
        return 'x = ' + ', '.join([ans1, ans2])

    except ValueError:
        sqroot = sqrt(-radical)

        return 'No real answer'
    
    except ZeroDivisionError:
        return '"a" cannot be zero'


while True:
    a = int(input('Value of a: '))
    b = int(input('Value of b: '))
    c = int(input('Value of c: '))
    print()

    print(quad_equation(a, b, c))