from math import cos
from math import sin

class LawOfSine():
    
    @staticmethod
    def los_find_length():
        pass

    @staticmethod
    def los_find_angle():
        pass

class LawOfCos():
    @staticmethod
    def loc_find_length():
        pass

    def loc_find_angle():
        pass

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

            ans = (a_side * sin(b_angle)) / sin(a_angle)

    elif menu == '2':
        pass

    elif menu == '3':
        menu_loop = False

else:
    pass