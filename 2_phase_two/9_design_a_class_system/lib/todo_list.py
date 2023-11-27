from lib.todo import Todo
class TodoList:
    def __init__(self):
        self.to_do_list = []

    def add(self, todo):
        self.to_do_list.append(todo)

    def return_filtered_list(self, filter):
        return_list = []
        for item in self.to_do_list:
            if item.return_status() is filter:
                return_list.append(self.format_result(item))
        return "\n".join(return_list)

    def format_result(self, list_item):
        if list_item.return_status():
            return list_item.return_task() + " - Complete"
        else:
            return list_item.return_task() + " - Incomplete"
    def incomplete(self):
        return self.return_filtered_list(False)

    def complete(self):
        return self.return_filtered_list(True)

    def all(self):
        return_list = []
        for item in self.to_do_list:
            return_list.append(self.format_result(item))
        return "\n".join(return_list)

    def give_up(self):
        for item in self.to_do_list:
            item.mark_complete()
