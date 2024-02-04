from math import pi

class Area:
    @staticmethod
    def circle_area_func(radius):
        return pi * radius ** 2
    
    @staticmethod
    def rectangle_area_func(side1, side2):
        return side1 * side2

    @staticmethod
    def trapezoid_area_func(base1, base2, height):
        return ((base1 + base2) / 2) * height

    @staticmethod
    def triangle_area_func(side1, side2):
        return (side1 * side2) / 2

if __name__ == '__main__':
    options_loop = True
    while options_loop:
        options = input('''Choose a shape:
    1) Circle
    2) Rectangle
    3) Trapezoid
    4) Triangle\n\n''').lower().strip()

        if options == 'circle' or options == '1':
            shape_parameter_loop = True
            while shape_parameter_loop:
                try:
                    radius = float(input('\nRadius: ').strip())
                    print(Area.circle_area_func(radius))
                    print()

                    shape_parameter_loop = False

                except ValueError:
                    pass

        elif options == 'rectangle' or options == '2':
            shape_parameter_loop = True
            while shape_parameter_loop:
                try:
                    side1 = float(input('\nSide 1: ').strip())
                    side2 = float(input('Side 2: ').strip())
                    print(Area.rectangle_area_func(side1, side2))

                    shape_parameter_loop = False

                except ValueError:
                    pass

        elif options == 'trapezoid' or options == '3':
            shape_parameter_loop = True
            while shape_parameter_loop:
                try:
                    base1 = float(input('\nBase 1: ').strip())
                    base2 = float(input('Base 2: ').strip())
                    height = float(input('Height: ').strip())
                    print(Area.trapezoid_area_func(base1, base2, height))

                    shape_parameter_loop = False

                except ValueError:
                    pass

        elif options == 'triangle' or options == '4':
            shape_parameter_loop = True
            while shape_parameter_loop:
                try:
                    side1 = float(input('\nSide 1: ').strip())
                    side2 = float(input('Side 2: ').strip())
                    print(Area.rectangle_area_func(side1, side2))

                    shape_parameter_loop = False

                except ValueError:
                    pass

        else:
            pass
