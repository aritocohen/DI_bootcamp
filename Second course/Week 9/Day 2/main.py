class Task:
    def __init__(self, content, date):
        """

        """
        self.content    =   content
        self.date       =   date



class TodoList:
    def __init__(self, name):
        """

        """
        self.name = name
        self.list_of_tasks  =  []


     def display_list(self):
        """

        """
        print("Upcoming tasks:")
        for task in self.list_of_tasks:
            print(f"({task.date}) {task.content}")

            
    def add_task(self, task):
        """

        """
        self.list_of_tasks.append(task)

todo_list = TodoList("My TODO List")

task1 = Task("Learn python", "Saturday 26.12")
task2 = Task("Learn python", "Sunday 27.12")
task3 = Task("Learn python", "Monday 28.12")

todo_list.add_task(task1)
todo_list.add_task(task2)
todo_list.add_task(task3)

todo_list.display_list()