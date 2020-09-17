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


mass_list = get_mass_from_file()
fuel = fuel_required_for_list(mass_list)
print(fuel)
