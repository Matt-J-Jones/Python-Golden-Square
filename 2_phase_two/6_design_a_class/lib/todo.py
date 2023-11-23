class ToDo:
    def __init__(self):
        self.task_list = {}

    def print_list(self):
        active_tasks = []
        for key in self.task_list:
            if self.task_list[key] is True:
                active_tasks.append(key)
        return ", ".join(active_tasks)

    def add(self, task):
        if task is None or task == "":
            raise Exception("Task cannot be empty")
        self.task_list[task] = True

    def mark_complete(self, task):
        if task in self.task_list:
            self.task_list[task] = False
