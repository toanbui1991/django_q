from time import sleep

def sleep_and_print(secs):
    sleep(secs)
    print("Task ran!")

def print_result(task):
    print(task.result)