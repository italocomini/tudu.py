_tasks_repository = [
    {'id': '1', 'title': 'Task 1'},
    {'id': '2', 'title': 'Task 2'},
    {'id': '3', 'title': 'Task 3'},
]


def get_tasks():
    return _tasks_repository


def get_task_by_id(task_id):
    task = [task for task in _tasks_repository if task['id'] == task_id]
    return task
