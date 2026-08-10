def calculate_fuel(mass):
    return (mass // 3) - 2


fuel_required = 0
with open("../input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        fuel_required += calculate_fuel(int(line.strip()))

print(f"Total fuel required: {fuel_required}")
