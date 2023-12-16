import random
import string
def forty_characters():
    characters = string.ascii_letters + string.digits + string.punctuation
    forty_characters = ''.join(random.choice(characters) for _ in range(40))
    print(forty_characters)
print('')