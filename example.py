import secret
from rtm import createRTM

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
                    tasks.append(Task(t))
            else:
                tasks.append(Task(l.taskseries))

    return tasks

def add(string):
    rtm = createRTM(secret.API_KEY, secret.SHARED_SECRET, secret.TOKEN)
    time = rtm.timelines.create()
    rtm.tasks.add(timeline=time.timeline, name=string, parse=1)
    return
 

