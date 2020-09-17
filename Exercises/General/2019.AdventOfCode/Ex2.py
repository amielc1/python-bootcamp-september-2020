# https://adventofcode.com/2019/day/2
# Here are the initial and final states of a few more small programs:
#
# 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
# 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
# 2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
# 1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.

map_list = [1, 0, 0, 0, 99]

temp = map_list[:4:1]

print(temp)
print(map_list)
