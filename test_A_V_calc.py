#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pytest
from A_V_calc import area_rectangle, area_circle, area_triangle, volume_cube, volume_cylinder

# Test for area_rectangle
def test_area_rectangle():
    assert area_rectangle(3, 4) == 12
    assert area_rectangle(5, 2) == 10
    assert area_rectangle(0, 4) == 0

# Test for area_circle
def test_area_circle():
    assert area_circle(3) == pytest.approx(28.274, 0.001)  # Using approx for float
    assert area_circle(1) == pytest.approx(3.141, 0.001)
    assert area_circle(0) == 0

# Test for area_triangle
def test_area_triangle():
    assert area_triangle(3, 4) == 6
    assert area_triangle(5, 2) == 5
    assert area_triangle(0, 4) == 0

# Test for volume_cube
def test_volume_cube():
    assert volume_cube(3) == 27
    assert volume_cube(2) == 8
    assert volume_cube(0) == 0

# Test for volume_cylinder
def test_volume_cylinder():
    assert volume_cylinder(3, 4) == pytest.approx(113.097, 0.001)
    assert volume_cylinder(1, 1) == pytest.approx(3.141, 0.001)
    assert volume_cylinder(0, 4) == 0
    


# In[ ]:




