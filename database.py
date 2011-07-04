from datetime import datetime, date
from django.forms import Select, ChoiceField
import pickle

class Task:
    def __init__(self, i, t, l = None, d = None, r = None, te = None, ta = None, p = None):
        self.id = i
        self._text = t
        self._list = l
        self._due = d
        self._repeat = r
        self._time_estimate = te
        self._tags = ta
        self._priority = p

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
    inp = open('data.pkl', 'rb')
    tasks = pickle.load(inp)
    inp.close()
    if _id is None:
        return tasks
    
    for task in tasks:
        print task.id, _id
        if task.id == int(_id):
            print "bingo"
            return task
    return None

def init():
    tasks = []
    tasks.append(Task(1, "Task jedan", None, datetime(2011, 7, 5, 10, 13), None, None, None, 1))
    tasks.append(Task(2, "Task dva", None, date(2011, 7, 6), None, None, None, 2))
    tasks.append(Task(3, "Task tri", None, None, None, None, None, 3))
    tasks.append(Task(4, "Task cetiri", None, None, None, None, None, None))

    output = open('data.pkl', 'wb')

    pickle.dump(tasks, output)

    output.close()
