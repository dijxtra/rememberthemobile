import secret
from django import forms
from datetime import date, datetime
from rtm import createRTM

class Task:
    def __init__(self, rtm, tasklist, taskseries, task = None):
        if task is None:
            task = taskseries.task

        self._rtm = rtm
        self.id = task.id
        self.series_id = taskseries.id
        self.list_id = tasklist.id
        self._text = taskseries.name
        self._list = None
        if task.due == '':
            self._due = None
        else:
            self._due = datetime.strptime(task.due, "%Y-%m-%dT%H:%M:%SZ")
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
            return ''

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
            return ''

        day = self._due.strftime("%Y-%m-%d")

        if type(self._due) is datetime:
            time = self._due.strftime(" %H:%M")
            return day + time
        if type(self._due) is date:
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
        return forms.ChoiceField(choices = [(0, ''), (1, '1'), (2, '2'), (3, '3')], widget = forms.Select)

    def toConsole(self):
        retval = self.text()

        if self.due() != '':
            retval += ' ' + self.due()

        if self.priority() != '':
            retval += ' !' + self.priority()

        return retval

    def complete(self):
        self._rtm.tasks.complete(timeline = self._rtm.timeline, list_id = self.list_id, taskseries_id = self.series_id, task_id = self.id)

    def postpone(self):
        self._rtm.tasks.postpone(timeline = self._rtm.timeline, list_id = self.list_id, taskseries_id = self.series_id, task_id = self.id)

def get_date(date):

    rtm = createRTM(secret.API_KEY, secret.SHARED_SECRET, secret.TOKEN)

    rspTasks = rtm.tasks.getList(filter='due:' + date)
    tasks = []
    if hasattr(rspTasks.tasks, "list") and \
        hasattr(rspTasks.tasks.list, "__getitem__"):
        for l in rspTasks.tasks.list:
            # XXX: taskseries *may* be a list
            if isinstance(l.taskseries, (list, tuple)):
                for t in l.taskseries:
                    tasks.append(Task(rtm, l, t))
            else:
                tasks.append(Task(rtm, l, l.taskseries))

    return tasks

def get_task(list_id, series_id, task_id):

    rtm = createRTM(secret.API_KEY, secret.SHARED_SECRET, secret.TOKEN)

    rspTasks = rtm.tasks.getList()
    tasks = []
    if hasattr(rspTasks.tasks, "list") and \
        hasattr(rspTasks.tasks.list, "__getitem__"):
        for l in rspTasks.tasks.list:
            # XXX: taskseries *may* be a list
            if not hasattr(l, "taskseries"):
                continue
            if isinstance(l.taskseries, (list, tuple)):
                for taskserie in l.taskseries:
                    if isinstance(taskserie.task, (list, tuple)):
                        for task in taskserie.task:
                            t = Task(rtm, l, taskserie, task)
                            if t.list_id == list_id and t.series_id == series_id and t.id == task_id:
                                return t
                    else:
                        t = Task(rtm, l, taskserie)
                        if t.list_id == list_id and t.series_id == series_id and t.id == task_id:
                            return t
            else:
                t = Task(rtm, l, l.taskseries)
                if t.list_id == list_id and t.series_id == series_id and t.id == task_id:
                    return t

    return None

def add(string):
    rtm = createRTM(secret.API_KEY, secret.SHARED_SECRET, secret.TOKEN)
    time = rtm.timelines.create()
    rtm.tasks.add(timeline=time.timeline, name=string, parse=1)
    return
 

