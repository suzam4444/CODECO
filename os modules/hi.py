import random
import string
chars=string.ascii_letters
r1="".join(random.choice(chars) for _ in range(3))
print(r1)