

class Employee:
    def __init__(self, id_employees, employees_name):
        self.id_employees = id_employees
        self.employees_name = employees_name
        self.list_of_task = []

    def add_task(self, task_id, task_description):
        task = Task(task_id, task_description)
        self.list_of_task.append(task)

    def complete_task(self, task_id):
        pass #for i in list_of_task

    def print_details(self):
        print(f"employee\n id:{self.id_employees}\n list of task{self.list_of_task}")

class Manager(Employee):
    def __init__(self, id_employees, employees_name, list_of_employees):
        super().__init__()
        self.list_of_employees = []

    def







class Task:
    def __init__(self, task_id, task_description):
        self.task_id = task_id
        self.task_description = task_description
