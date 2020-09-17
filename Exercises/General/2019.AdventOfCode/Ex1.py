# https://adventofcode.com/2019/day/1
# For a mass of 100756, the fuel required is 33583.
# 100756 / 3
# rund down
# -2
# For a mass of 1969, the fuel required is 654.
import math


def fuel_required(mass):
    mass /= 3
    mass = math.trunc(mass)
    mass -= 2
    return mass


def get_mass_from_file():
    with open('mass_list.txt', 'r') as f:
        mass_list = [int(line) for line in f]
        return mass_list


def fuel_required_for_list(mass_list):
    counter = 0
    for mass in mass_list:
        counter += fuel_required(mass)
    return counter


def get_total_fuel(mass):
    total_fuel = 0
    fuel_result = 0
    fuel_result = fuel_required(mass)
    while fuel_result > 0:
        total_fuel += fuel_result
        fuel_result = fuel_required(fuel_result)
    return total_fuel


# mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
get_total_fuel(100756)

# mass_list = get_mass_from_file()
# fuel = fuel_required_for_list(mass_list)
# print(fuel)


mass_list = get_mass_from_file()
total_fuel_list = list(map(lambda x: get_total_fuel(x), mass_list))
print(sum(total_fuel_list))
total = 0
for m in mass_list:
    total += get_total_fuel(m)
print(total)
