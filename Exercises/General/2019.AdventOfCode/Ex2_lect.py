import operator


class IntcodeComputer:
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input
        self.ip = 0
        self.running = True

    def result(self):
        return self.puzzle_input[0]

    def get_next_instruction(self):
        op, inp_ind1, inp_ind2, out_ind = self.puzzle_input[self.ip:self.ip + 4]
        self.ip += 4
        if op == 1:
            return [self.add, [inp_ind1, inp_ind2, out_ind]]
        elif op == 2:
            return [self.mul, [inp_ind1, inp_ind2, out_ind]]
        elif op == 99:
            return [self.stop, []]

    def do_math(self, op, inp_idx1, inp_idx2, out_idx):
        self.puzzle_input[out_idx] = op(self.puzzle_input[inp_idx1], self.puzzle_input[inp_idx2])

    def add(self, inp_idx1, inp_idx2, out_idx):
        self.do_math(operator.add, inp_idx1, inp_idx2, out_idx)

    def mul(self, inp_idx1, inp_idx2, out_idx):
        self.do_math(operator.mul, inp_idx1, inp_idx2, out_idx)

    def stop(self):
        self.running = False


vm = IntcodeComputer([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])

while vm.running:
    op, params = vm.get_next_instruction()
    op(*params)

print(vm.result())
