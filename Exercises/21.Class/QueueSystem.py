class Person():
    def __init__(self, name):
        self.name = name


class Worker:
    def __init__(self, worker_name):
        self.worker_name = worker_name
        self.persons = []

    def add_person(self, person: Person):
        print(f"add {person.name} to {self.worker_name} queue")
        self.persons.append(person)

    def get_person(self):
        poped_person: Person = self.persons.pop()
        print(f'remove {poped_person.name} from {self.worker_name} queue')


class Command:

    def __init__(self):
        self.command_type: str
        self.person: str
        self.worker: str
        self.workers = {}

    def parse_input(self, input_str):
        command_list = input_str.split()
        self.command_type = command_list[0]
        self.worker = command_list[1]
        self.person = command_list[2]

    def get_worker(self, worker_name):
        if not worker_name in workers:
            worker = Worker(worker_name)
            workers[worker_name] = worker
        return workers[worker_name]

    def parse_command(self, command: str):
        command_list = command.split()
        self.command_type = command_list[0]
        self.worker = self.get_worker(command_list[1])
        if command_list > 2:
            self.worker.add_person(command_list[2])

    def __add_woeker_to_list__(self):
        pass


if True:
    cmd_input = input()
    cmd = Command()
    cmd.parse_input(cmd_input)
    w1 = Worker("Amiel")
    w1.persons.append(Person("Amiel_p1"))
    w1.persons.append(Person("Amiel_p2"))
    w2 = Worker("Talya")
    w2.persons.append(Person("Talya_p1"))
    w2.persons.append(Person("Talya_p2"))
    workers = {}
    workers[w1.worker_name] = w1
    workers[w2.worker_name] = w2
    while True:
        if cmd.command_type == "next":
            print(workers[cmd.worker].persons.pop(0).name)
        if cmd.command_type == "wait":
            pass

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
