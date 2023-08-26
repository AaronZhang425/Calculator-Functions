from math import *

a = 0
b = 0
c = 0


def pythagorean_theorem(prompt, a, b, c):
  if prompt == 'c':
    c = (a**2) + (b**2)
    c = sqrt(c)
    return c

  elif prompt == 'a':
    a = (c**2) - (b**2)
    a = sqrt(a)
    return a

  elif prompt == 'b':
    b = (c**2) - (a**2)
    b = sqrt(b)
    return b


prompt_loop = True
while prompt_loop:
  prompt = input('Find: ').lower().strip()

  if prompt == 'c':
    value_loop = True
    while value_loop:
      try:
        a = float(input('Value of a: ').strip())
        b = float(input('Value of b: ').strip())

        if a >= 0 and b >= 0:
          print(f'{prompt} is equal to {pythagorean_theorem(prompt, a, b, c)}')
          print()
          value_loop = False

        else:
          pass

      except ValueError:
        pass

    value_loop = False

  elif prompt == 'a':
    value_loop = True
    while value_loop:
      try:
        b = float(input('Value of a: ').strip())
        c = float(input('Value of b: ').strip())

        if b >= 0 and c >= 0:
          print(f'{prompt} is equal to {pythagorean_theorem(prompt, a, b, c)}')
          print()
          value_loop = False

        else:
          pass

      except ValueError:
        pass

    value_loop = False

  elif prompt == 'b':
    value_loop = True
    while value_loop:
      try:
        b = float(input('Value of a: ').strip())
        c = float(input('Value of b: ').strip())

        if b >= 0 and c >= 0:
          print(f'{prompt} is equal to {pythagorean_theorem(prompt, a, b, c)}')
          print()
          value_loop = False

        else:
          pass

      except ValueError:
        pass

    value_loop = False

  elif prompt == 'quit':
    prompt_loop = False
    value_loop = False

  else:
    print('Please enter a, b, c, or quit to exit.')
