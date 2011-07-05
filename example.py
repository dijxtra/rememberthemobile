import secret
import database
from rtm import createRTM

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
                    tasks.append(database.Task(t))
            else:
                tasks.append(database.Task(l.taskseries))

    return tasks

def add(string):
    rtm = createRTM(secret.API_KEY, secret.SHARED_SECRET, secret.TOKEN)
    time = rtm.timelines.create()
    rtm.tasks.add(timeline=time.timeline, name=string, parse=1)
    return
 

