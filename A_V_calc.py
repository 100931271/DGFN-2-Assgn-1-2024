#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function 1: Area of a Rectangle
def area_rectangle(length, width):
    """Calculate the area of a rectangle."""
    return length * width

# Function 2: Area of a Circle
import math

def area_circle(radius):
    """Calculate the area of a circle."""
    return math.pi * (radius ** 2)

# Function 3: Area of a Triangle
def area_triangle(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

# Function 4: Volume of a Cube
def volume_cube(side):
    """Calculate the volume of a cube."""
    return side ** 3

# Function 5: Volume of a Cylinder
def volume_cylinder(radius, height):
    """Calculate the volume of a cylinder."""
    return math.pi * (radius ** 2) * height

# Menu display
def display_menu():
    print("\nA/V Calculator Menu")
    print("Q/q: Quit")
    print("V/v: Change View (Show Equation)")
    print("D/d: Default View (Show Result Only)")
    print("1: Area of a Rectangle")
    print("2: Area of a Circle")
    print("3: Area of a Triangle")
    print("4: Volume of a Cube")
    print("5: Volume of a Cylinder")

# Main calculator logic
def main():
    view_mode = 'D'  # Default view (just calculation)
    
    while True:
        display_menu()
        choice = input("Choose an option: ").lower()
        
        if choice == 'q':
            print("Quitting program...")
            break
        elif choice == 'v':
            view_mode = 'V'
        elif choice == 'd':
            view_mode = 'D'
        elif choice == '1':
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            result = area_rectangle(length, width)
            if view_mode == 'V':
                print(f"{length} * {width} = {result} (length * width = area)")
            else:
                print(f"Area = {result}")
        elif choice == '2':
            radius = float(input("Enter radius: "))
            result = area_circle(radius)
            if view_mode == 'V':
                print(f"{math.pi} * {radius}^2 = {result} (π * radius² = area)")
            else:
                print(f"Area = {result}")
        elif choice == '3':
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            result = area_triangle(base, height)
            if view_mode == 'V':
                print(f"0.5 * {base} * {height} = {result} (0.5 * base * height = area)")
            else:
                print(f"Area = {result}")
        elif choice == '4':
            side = float(input("Enter side length: "))
            result = volume_cube(side)
            if view_mode == 'V':
                print(f"{side}^3 = {result} (side³ = volume)")
            else:
                print(f"Volume = {result}")
        elif choice == '5':
            radius = float(input("Enter radius: "))
            height = float(input("Enter height: "))
            result = volume_cylinder(radius, height)
            if view_mode == 'V':
                print(f"{math.pi} * {radius}^2 * {height} = {result} (π * radius² * height = volume)")
            else:
                print(f"Volume = {result}")
        else:
            print("Invalid choice, try again.")

# Guard clause to prevent the script from executing when imported
if __name__ == "__main__":
    main()


# In[ ]:




