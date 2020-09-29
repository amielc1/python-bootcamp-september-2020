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

"""
Uri's comments:
==============

* Very good! This code works.
* File names and folder names, it's better to write in lowercase (like variable names) and then 
  import from the name in lowercase.
* Lines 16 and 17 are not necessary. Why do you need them?

"""
