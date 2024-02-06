import math

a_side = 0
a_angle = 0
b_side = 0
b_angle = 0
c_side = 0
c_angle = 0

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
        sub_menu = input('\nMENU:\n1. Find Angle\n2. Find Side\n').lower().strip()

        if sub_menu == '1':
            try:
                a_angle = float(input('Angle of A in degrees: ').strip())
                a_side = float(input('Length of side opposite to angle A:').strip())
                b_angle = float(input('Angle of B in degrees:').strip())
            
            except ValueError:
                print('Please enter a proper value\n')

        pass

    elif menu == '3':
        menu_loop = False

else:
    pass