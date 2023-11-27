class Todo:

    def __init__(self, task):
        self.task = {"Task": task, "Complete": False}

    def mark_complete(self):
        self.task["Complete"] = True

    def return_task(self):
        return self.task["Task"]

    def return_status(self):
        return self.task["Complete"]

