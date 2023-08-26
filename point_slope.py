def point_slope_equation(point1x, point1y, point2x, point2y):
    try:
        m = (point2y - point1y) / (point2x - point1x)
        b = m * point1x - point1y

        if b == 0:
            return f'y = {m}x'
        
        elif b > 0:
            return f'y = {m}x - {b}'
        
        else:
            return f'y = {m}x + {-b}'

    except ZeroDivisionError:
        return 'No slope'


while True:
    try:
        point1x = float(input('Point 1 x value: ').strip())
        point1y = float(input('Point 1 y value: ').strip())
        point2x = float(input('Point 2 x value: ').strip())
        point2y = float(input('Point 2 y value: ').strip())

        print(point_slope_equation(point1x, point1y, point2x, point2y))
        print()

    except ValueError:
        pass