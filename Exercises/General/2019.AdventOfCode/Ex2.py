# https://adventofcode.com/2019/day/2
# Here are the initial and final states of a few more small programs:
#
# 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
# 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
# 2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
# 1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.


map_list = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 19, 9, 23, 1, 23, 6, 27, 1, 9, 27, 31, 1,
            31, 10, 35, 2, 13, 35, 39, 1, 39, 10, 43, 1, 43, 9, 47, 1, 47, 13, 51, 1, 51, 13, 55, 2, 55, 6, 59, 1, 59,
            5, 63, 2, 10, 63, 67, 1, 67, 9, 71, 1, 71, 13, 75, 1, 6, 75, 79, 1, 10, 79, 83, 2, 9, 83, 87, 1, 87, 5, 91,
            2, 91, 9, 95, 1, 6, 95, 99, 1, 99, 5, 103, 2, 103, 10, 107, 1, 107, 6, 111, 2, 9, 111, 115, 2, 9, 115, 119,
            2, 13, 119, 123, 1, 123, 9, 127, 1, 5, 127, 131, 1, 131, 2, 135, 1, 135, 6, 0, 99, 2, 0, 14, 0]


# map_list = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,6,27,1,9,27,31,1,31,10,35,2,13,35,39,1,39,10,43,1,43,9,47,1,47,13,51,1,51,13,55,2,55,6,59,1,59,5,63,2,10,63,67,1,67,9,71,1,71,13,75,1,6,75,79,1,10,79,83,2,9,83,87,1,87,5,91,2,91,9,95,1,6,95,99,1,99,5,103,2,103,10,107,1,107,6,111,2,9,111,115,2,9,115,119,2,13,119,123,1,123,9,127,1,5,127,131,1,131,2,135,1,135,6,0,99,2,0,14,0]


class Command():
    def __init__(self, cmd_list: list, origin_list: list):
        self.cmd_type = cmd_list[0]
        self.left_op_index = cmd_list[1]
        self.right_op_index = cmd_list[2]
        self.result_index = cmd_list[3]
        self.orighin_list = origin_list

    def colculate_commnad(self):
        if self.cmd_type == 1:
            result = self.orighin_list[self.left_op_index] + self.orighin_list[self.right_op_index]
            self.orighin_list[self.result_index] = result
        if self.cmd_type == 2:
            result = self.orighin_list[self.left_op_index] * self.orighin_list[self.right_op_index]
            self.orighin_list[self.result_index] = result


print(map_list)

# last = 0
# index = 4
# while index < len(map_list):
#     cmd = Command(map_list[last:index], map_list)
#     cmd.colculate_commnad()
#     last = index
#     index += 4
#

for i in range(0, len(map_list), 4):
    slice = map_list[i:i + 4]
    if len(slice) == 4:
        cmd = Command(slice, map_list)
        cmd.colculate_commnad()

print(map_list)
