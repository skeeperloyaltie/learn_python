import math
import random

def is_square(n):
    if n < 0:
        return False
    
    squareroot = n ** 0.5
    
    if squareroot % 1 == 0:
        return True
    else:
        return False

n = random.randint(1,10)
print(n)

print(is_square(n))