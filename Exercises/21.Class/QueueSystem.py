class Person():
    pass


class Worker:
    def __init__(self):
        self.persons = []

    def add_person(self, person: Person):
        self.persons.append(person)

    def get_person(self):
        return self.persons.pop()


class Command:
    def __init__(self):
        self.command_type: str
        self.person: str
        self.worker: str

    def parse_command(self, command: str):
        command_list = command.split()
        self.command_type = command_list[0]
        self.worker = command_list[1]
        self.person = command_list[2]


workers = []
cmd = Command()
cmd.parse_command("wait dave mika")
if cmd.command_type == "wait":
    worker = workers[cmd.worker]
# > python3 queue.py
# : wait dave mika
# : wait dave jane
# : wait dave bill
# : wait michael eddy
# : wait michael jim
#
# : next dave
# mika
#
# : next dave
# jane
#
# : next michael
# eddy
