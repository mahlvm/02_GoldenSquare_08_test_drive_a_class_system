class Todo:

#   Sets the task property
#   Sets the complete property to False
    def __init__(self, task):
        self.task = task
        self.status = False



#   Sets the complete property to True
    def mark_complete(self):
            self.status = True