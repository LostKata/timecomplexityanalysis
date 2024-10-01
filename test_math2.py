import pytest
from math2 import Vec2, quadsolve, max2


def test_vec2_length():
    a = Vec2(3,4)
    b = Vec2(0,0)
    assert a.length() == 5.0
    assert b.length() == 0.0

def test_vec2_init_invalid_values():
    with pytest.raises(ValueError, match="vector components must"):
        a = Vec2(1, "two")

    with pytest.raises(ValueError, match="vector components must"):
        a = Vec2("one", 2)

    with pytest.raises(ValueError, match="vector components must"):
        a = Vec2(1, (2,3))

def test_vec2_print():
    a = Vec2(1,1)
    assert a.__str__() == "Vector 2D (x: 1.0, y: 1.0)"
    
# Test af quadsolve
def test_quadsolve_two_real_roots():
    roots = quadsolve(1, -3, 2, 0)
    assert len(roots) == 2

def test_one_real_roots():
    roots = quadsolve(1, -2, 1, 0)
    assert len(roots) == 1
    
def test_no_real_roots():
    roots = quadsolve(1,1,1,0)
    assert len(roots) == 0
    
