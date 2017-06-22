# To design this simulation we will create classes for the three real-world objects
# Printer, Task, and PrintQueue.


import random
from printer import Printer
from task import Task
from Q.queue import Queue


def simulation(num_seconds, pages_per_minute, num_students):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task(num_students):
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.de_queue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)

    print(f"Average Wait {average_wait:6.2f} secs {print_queue.size():3d} tasks remaining.")


def new_print_task(num_students):
    num = random.randrange(1, (3600/num_students)+1)
    if num == num_students:
        return True
    else:
        return False

for i in range(10):
    simulation(3600, 5, 50)

