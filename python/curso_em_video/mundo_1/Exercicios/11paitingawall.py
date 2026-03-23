# Create a program that reads the width and height of a wall and calculates how much paint is needed to cover it.
# Consider that 1 liter of paint covers 2 square meters of wall.

wall_width = float(input("What is the width of the wall? "))
wall_height = float(input("What is the height of the wall? "))
wall_area = wall_width * wall_height
paint_needed = wall_area / 2
print(f"The wall's area is {wall_area:.2f} and you will need {paint_needed:.2f} liters of paint to cover it.")