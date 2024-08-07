import math

class LawOfSine():
    
    @staticmethod
    def los_find_length(a_side, a_angle, b_angle):
        side_length = a_side \
            * math.sin(math.radians(b_angle)) / math.sin(math.radians(a_angle))
        
        return side_length

    @staticmethod
    def los_find_angle(a_side, a_angle, b_side):
        angle_measure = math.asin((
            b_side * math.sin(math.radians(a_angle)))
            / a_side
            )
            
        return angle_measure

class LawOfCos():
    @staticmethod
    def loc_find_length(a_side, b_side, c_angle):
        side_length = math.sqrt(
            a_side**2
            + b_side**2
            - 2 * a_side * b_side * math.cos(math.radians(c_angle))
        )

        return side_length


    @staticmethod
    def loc_find_angle(a_side, b_side, c_side):
        angle_rad = math.acos(
            (c_side**2 - (a_side**2 + b_side**2)) / -2 
            * a_side 
            * b_side
        )

        return math.degrees(angle_rad)

menu_loop = True
while menu_loop:
    menu = input('MENU:\n1. Law of Sine\n2. Law of Cosine\n3. Exit\n').strip()

    if menu == '1':
        sub_menu = input('\nMENU:\n1. Find angle\n2. Find side length\n').strip()

        if sub_menu == '1':
            input_value_loop = True
            while input_value_loop:
                try:
                    a_angle = float(input('\nAngle of A in degrees: ').strip())
                    a_side = float(input('Length of side opposite to angle A: ').strip())
                    b_side = float(input('Length of side B: ').strip())
                
                    input_value_loop = False

                except ValueError:
                    print('Please enter a proper value')
                
            print(f'\nAngle B is: {LawOfSine.los_find_angle(a_angle, a_side, b_side)} degrees\n')

        elif sub_menu == '2':
            input_value_loop = True
            while input_value_loop:
                try:
                    a_angle = float(input('\nAngle of A in degrees: ').strip())
                    a_side = float(input('Length of side opposite to angle A: ').strip())
                    b_angle = float(input('Angle of B in degrees: ').strip())

                    input_value_loop = False

                except ValueError:
                    print('Please enter a proper value')

            print(f'\nThe length B is: {LawOfSine.los_find_length(a_side, a_angle, b_angle)}\n')

    elif menu == '2':
        sub_menu = input('\nMENU:\n1. Find angle\n2. Find side length\n').strip()

        if sub_menu == '1':
            input_value_loop = True
            while input_value_loop:
                try:
                    a_side = float(input('\nLength of side A: ').strip())
                    b_side = float(input('Length of side B: ').strip())
                    c_side = float(input('Length of side C: ').strip())

                    input_value_loop = False
                
                except ValueError:
                    print('Please enter a proper value')
                
            print(f'\nThe anlge opposite to side C measures {LawOfCos.loc_find_angle(a_side, b_side, c_side)} degrees\n')

        elif sub_menu == '2':
            input_value_loop = True
            while input_value_loop:
                try:
                    a_side = float(input('\nLength of side A: ').strip())
                    b_side = float(input('Length of side B: ').strip())
                    c_angle = float(input('Measure of angle adjacent to sides A and B: ').strip())

                    input_value_loop = False
                
                except ValueError:
                    print('Please enter a proper value')
                
            print(f'\nThe side opposite to angle C measures {LawOfCos.loc_find_length(a_side, b_side, c_angle)}\n')

    elif menu == '3':
        menu_loop = False

else:
    pass