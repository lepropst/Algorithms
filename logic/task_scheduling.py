import datetime
from dateutil import parser


class task:
    def __init__(self, start: str, end: str) -> None:
        if parser.parse(start) and parser.parse(end):
            self.start = parser.parse(start)
            self.end = parser.parse(end)
        else:
            raise InterruptedError

    def __lt__(self, next):
        return self.start < next.start


def schedule_tasks(tasks: list[task], machines=1):
    availableMachines = {}
    for mach in range(0, machines):
        availableMachines[mach] = []

    while tasks:
        tasks.sort(key=lambda x: x.start)
        current_task = tasks.pop(0)
        for idx, machine in enumerate(availableMachines):
            print(idx)
            print(machine)
            if machine[len(machine) - 1].end < current_task.start:
                machine[len(machine) - 1].append(current_task)
                break
            else:
                if idx == len(availableMachines.keys()):
                    availableMachines[len(availableMachines.keys())] = [current_task]
                    break
                else:
                    continue
    for array in availableMachines:
        print(array)
