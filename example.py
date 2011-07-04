import secret
from rtm import createRTM

rtm = createRTM(secret.API_KEY, secret.SHARED_SECRET, secret.TOKEN)

rspTasks = rtm.tasks.getList(filter='due:"today"')
tasks = []
if hasattr(rspTasks.tasks, "list") and \
   hasattr(rspTasks.tasks.list, "__getitem__"):
    for l in rspTasks.tasks.list:
        # XXX: taskseries *may* be a list
        if isinstance(l.taskseries, (list, tuple)):
            for t in l.taskseries:
                tasks.append(t.name)
        else:
            tasks.append(l.taskseries.name)
print "\n".join(tasks)
if not tasks:
    tasks.append('No tasks due within a week')

