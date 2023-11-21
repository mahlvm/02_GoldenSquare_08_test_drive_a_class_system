from lib.todo import Todo
from lib.todo_list import TodoList

def test_add_to_list():
    todolist = TodoList()
    task_1 = Todo("Task 1")
    task_2 = Todo("Task 2")
    todolist.add(task_1)
    todolist.add(task_2)
    result = todolist.todo_list
    assert result == [task_1, task_2]

def test_incomplete_list():
    todolist = TodoList()
    task_1 = Todo("Task 1")
    task_2 = Todo("Task 2")
    task_3 = Todo("Task 3")
    todolist.add(task_1)
    todolist.add(task_2)
    todolist.add(task_3)
    result = todolist.incomplete()
    assert result == [task_1, task_2, task_3]

def test_mark_complete():
    todolist = TodoList()
    task_1 = Todo("Task 1")
    task_2 = Todo("Task 2")
    task_3 = Todo("Task 3")
    task_1.mark_complete()
    task_2.mark_complete()
    todolist.add(task_1)
    todolist.add(task_2)
    todolist.add(task_3)
    result = [task_1.status, task_2.status, task_3.status]
    assert result == [True, True, False]

def test_complete_list():
    todolist = TodoList()
    task_1 = Todo("Task 1")
    task_2 = Todo("Task 2")
    task_3 = Todo("Task 3")
    task_1.mark_complete()
    task_2.mark_complete()
    todolist.add(task_1)
    todolist.add(task_2)
    todolist.add(task_3)
    result = todolist.complete()
    assert result == [task_1, task_2]

def test_give_up():
    todolist = TodoList()
    task_1 = Todo("Task 1")
    task_2 = Todo("Task 2")
    task_3 = Todo("Task 3")
    todolist.add(task_1)
    todolist.add(task_2)
    todolist.add(task_3)
    todolist.give_up()
    result = [task_1.status, task_2.status, task_3.status]
    assert result == [True, True, True]

    
