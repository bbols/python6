import math
def many_one_add(a):
    try:
        a+=1
    except:
        pass
    return a

def many_filter(a):
    if a%2==0:
        return True
    return False

a=[1,2,3,4,5,6,7,8,9]
a_char=['a','s','d','7','4','c','b']
a_char2=['a','s','d','c','b']

print(list(map(many_one_add,a)))

print(list(filter(many_filter,a)))
a_char2.sort()
print(a_char2)

print(math.pi)
import os
print(os.listdir())