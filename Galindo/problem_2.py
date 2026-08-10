import math

circle = 2 * math.pi * (15 / 2) ** 2 / 20
triangle = 20**2 * math.sqrt(3) / 4 / 20
square = 18**2 / 18
print(f"Circle: {circle:.2f} area/unit_dough")
print(f"Triangle: {triangle:.2f} area/unit_dough")
print(f"Square: {square:.2f} area/unit_dough")
options = {"circle": circle, "triangle": triangle, "square": square}
best = max(options, key=options.get)
print(f"The best shape is {best} with a value of {options[best]} area/unit_dough.")
