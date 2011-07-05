from datetime import datetime, date
from django.forms import Select, ChoiceField
import pickle
import example

OUTPUT_FILE = 'data.pkl'

class Task:
#    def __init__(self, i, t, l = None, d = None, r = None, te = None, ta = None, p = None):
    def __init__(self, taskseries):
        task = taskseries.task
        self.id = task.id
        self._text = taskseries.name
        self._list = None
        self._due = None
        self._repeat = None
        self._time_estimate = None
        self._tags = None
        self._priority = task.priority

    def text(self):
        if self._text is None:
            return ''
        return self._text

    def list(self):
        return self._list

    def due(self):
        if self._due is None:
            return " "

        day = self._due.strftime("%d %b")

        if date.today().isocalendar()[1] == self._due.isocalendar()[1]:
            day = self._due.strftime("%a")

        if  type(self._due) is datetime:
            time = self._due.strftime(" %H:%M")
            return day + time
        if  type(self._due) is date:
            return day

        return self._due

    def longdue(self):
        if self._due is None:
            return " "

        day = self._due.strftime("%Y-%m-%d")

        if  type(self._due) is datetime:
            time = self._due.strftime(" %H:%M")
            return day + time
        if  type(self._due) is date:
            return day

        return self._due

    def repeat(self):
        return self._repeat

    def time_estimate(self):
        return self._time_estimate

    def tags(self):
        return self._tags

    def priority(self):
        return self._priority

    def priority_widget(self):
        return ChoiceField(choices = [(0, ''), (1, '1'), (2, '2'), (3, '3')], widget = Select)

def get(_id = None):
    inp = open(OUTPUT_FILE, 'rb')
    tasks = pickle.load(inp)
    inp.close()
    if _id is None:
        return tasks
    
    for task in tasks:
        if task.id == int(_id):
            return task
    return None

def get_web(date):
    return example.get_date(date)

def delete(_id):
    inp = open(OUTPUT_FILE, 'rb')
    tasks = pickle.load(inp)
    inp.close()
    
    for task in tasks:
        if task.id == int(_id):
            tasks.remove(task)

    output = open(OUTPUT_FILE, 'wb')
    pickle.dump(tasks, output)
    output.close()

    return None

def put(task):
    inp = open(OUTPUT_FILE, 'rb')
    tasks = pickle.load(inp)
    inp.close()

    id = 1
    for t in tasks:
        if t.id >= id:
            id = t.id + 1

    task.id = id
    
    tasks.append(task)

    output = open(OUTPUT_FILE, 'wb')
    pickle.dump(tasks, output)
    output.close()
    
    return

def init():
    tasks = []
    tasks.append(Task(1, "Task jedan", None, datetime(2011, 7, 5, 10, 13), None, None, None, 1))
    tasks.append(Task(2, "Task dva", None, date(2011, 7, 6), None, None, None, 2))
    tasks.append(Task(3, "Task tri", None, None, None, None, None, 3))
    tasks.append(Task(4, "Task cetiri", None, None, None, None, None, None))

    output = open(OUTPUT_FILE, 'wb')

    pickle.dump(tasks, output)

    output.close()
