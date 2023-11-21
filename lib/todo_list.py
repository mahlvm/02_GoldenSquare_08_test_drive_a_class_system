class TodoList:
    def __init__(self):
        self.todo_list = []


#   Adds the todo to the list of todos
    def add(self, todo):
        self.todo_list.append(todo)

# Returns a list of Todo instances representing the todos that are not complete
    def incomplete(self):
        list_incomplete = []
        for i in self.todo_list:
            if i.status == False:
                list_incomplete.append(i)
        return list_incomplete


# Returns a list of Todo instances representing the todos that are complete
    def complete(self):
        list_complete = []
        for i in self.todo_list:
            if i.status == True:
                list_complete.append(i)
        return list_complete



#   Marks all todos as complete
    def give_up(self):
        for i in self.todo_list:
            i.mark_complete()