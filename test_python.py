from many_f import many_one_add,many_filter
import math
#map
a=[1,2,3,4,5,6,7,8,9]
a_char=['a','s','d','7','4','c','b']
def test_map():
    assert list(map(many_one_add,a))==[2,3,4,5,6,7,8,9,10]
#filter
def test_filter():
    assert list(filter(many_filter,a))==[2,4,6,8]

def test_sort():
    temp_char=a_char
    temp_char.sort()
    assert  temp_char==['4', '7', 'a', 'b', 'c', 'd','s']

def test_sorted():
    temp_char = a_char
    assert sorted(temp_char)==['4', '7', 'a', 'b', 'c', 'd','s']
    assert sorted(temp_char) == ['4', '7', 'a', 'b', 'c', 'd','s']

def test_math():
    assert math.pi==3.141592653589793
    assert math.sqrt(4)==2
    assert math.pow(2,2)==4
    assert math.hypot(0,2)==2.0
    assert math.hypot(3, 2) == 3.605551275463989
