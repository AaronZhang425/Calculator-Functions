import math

class LawOfSine():
    
    @staticmethod
    def los_find_length(a_side, a_angle, b_angle):
        side_length = ((
            a_side * math.sin(b_angle))
            / math.sin(a_angle)
        )
        
        return math.degrees(side_length)

    @staticmethod
    def los_find_angle(a_side, a_angle, b_side):
        angle_rad = (
            math.asin((b_side * math.sin(a_angle))
            / a_side)
            )
        
        return math.degrees(angle_rad)

class LawOfCos():
    @staticmethod
    def loc_find_length(a_side, b_side, c_angle):
        side_length = math.sqrt(
            a_side**2
            + b_side**2
            - 2 * a_side * b_side * math.cos(c_angle)
        )

        return math.degrees(side_length)


    @staticmethod
    def loc_find_angle(a_side, b_side, c_side):
        b_side + a_side
        angle_rad = math.acos(
            (c_side**2 - (a_side**2 - b_side**2)) / -2 
            * a_side 
            * b_side
        )

        return math.degrees(angle_rad)

menu_loop = True
while menu_loop:
    menu = input('MENU:\n1. Law of Sine\n2. Law of Cosine\n3. Exit\n').strip().lower()

    if menu == '1':
        sub_menu = input('\nMENU:\n1. Find Angle\n2. Find Side Length\n').lower().strip()

        if sub_menu == '1':
            input_value_loop = True
            while input_value_loop:
                try:
                    a_angle = float(input('\nAngle of A in degrees: ').strip())
                    a_side = float(input('Length of side opposite to angle A: ').strip())
                    b_side = float(input('Lenght of side B: ').strip())
                
                    input_value_loop = False

                except ValueError:
                    print('Please enter a proper value')
                
            print(f'\nAngle B is: {LawOfSine.los_find_angle(a_angle, a_side, b_side)} degrees\n')

        elif sub_menu == '2':
            input_value_loop = True
            while input_value_loop:
                try:
                    a_angle = float(input('\nAngle of A in Degrees: ').strip())
                    a_side = float(input('Length of side opposite to angle A: ').strip())
                    b_angle = float(input('Angle of B in Degrees: ').strip())

                    input_value_loop = False

                except ValueError:
                    print('Please enter a proper value')

            print(f'\nThe length B is: {LawOfSine.los_find_length(a_angle, a_side, b_angle)}')

    elif menu == '2':
        sub_menu = input('\nMENU:\n1. Find Angle\n2. Find Side Length\n').lower().strip()

        if sub_menu == '1':
            pass

        elif sub_menu == '2':
            pass

    elif menu == '3':
        menu_loop = False

else:
    pass