class Widget:

    def __init__(self, name):
        self.name = name
        self.is_built = False
        self.dependency = []

    def add_dependency(self, *widgetes):
        # Easier to use:
        # self.dependency += widgets
        for widget in widgetes:
            print(f"{self.name} depend on {widget.name}")
            self.dependency.append(widget)

    def build(self):
        self.is_built = True
        for widget in self.dependency:
            if not widget.is_built:
                widget.build()
                print(f"Build {widget.name} for build {self.name}")


luke = Widget("Luke")
hansolo = Widget("Han Solo")
leia = Widget("Leia")
yoda = Widget("Yoda")
padme = Widget("Padme Amidala")
anakin = Widget("Anakin Skywalker")
obi = Widget("Obi-Wan")
darth = Widget("Darth Vader")
_all = Widget("Widget all")

luke.add_dependency(hansolo, leia, yoda)
leia.add_dependency(padme, anakin)
obi.add_dependency(yoda)
darth.add_dependency(anakin)

_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
_all.build()
# code should print: Han Solo, Padme Amidala, Anakin Skywalker, Leia, Yoda, Luke, Obi-Wan, Darth Vader
# (can print with newlines in between modules)
