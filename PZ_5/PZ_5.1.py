# Составить функцию, которая напечатает сорок любых символов.

import random
def print_random_chars():
    chars = [chr(random.randint(33, 126)) for _ in range(40)]
    print(''.join(chars))
print_random_chars()
