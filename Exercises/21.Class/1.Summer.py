class Summer:
    def __init__(self):
        self.total_value = 0

    def add(self, *values):
        self.total_value += sum(values)
    def print_total(self):
        print(self.total_value)

s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)
s.add()
t.add()
# should print 60
s.print_total()

# should print 50
t.print_total()
