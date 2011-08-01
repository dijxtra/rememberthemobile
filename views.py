from datetime import datetime, date
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
import datetime
import database

def index(request, date = None):
    date = datetime.date.today()

    return day(request, date.year, date.month, date.day)

def day(request, year, month, day):
    date = str(year).zfill(2) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)
    d = datetime.date(int(year), int(month), int(day))

    pre = d - datetime.timedelta(days = 1)
    today = datetime.date.today()
    post = d + datetime.timedelta(days = 1)
    
    tasks = database.get_date(date)

    tasks = sorted(tasks, key = lambda task: task.priority())
    
    head_days = ['today', '&larr;', date, '&rarr;']
    head_links = [today.strftime('/%Y/%m/%d/'), pre.strftime('/%Y/%m/%d/'), '', post.strftime('/%Y/%m/%d/')]

    d = {'tasks': tasks, 'head_days': head_days, 'head_links': head_links}
    return render_to_response('index.html', d, RequestContext(request))

def action(request):
    if request.POST['submit'] == 'add':
        return add(request)
    if request.POST['submit'] == 'search':
        return search(request)
    return index(request)
    

def add(request):
    text = request.POST['text']
    database.add(text)
    return redirect('home')

def delete(request, id):
    return index(request)

def search(request):
    text = request.POST['text']
    return index(request,text)

def edit(request, list_id, series_id, task_id):
    task = database.get_task(list_id, series_id, task_id)
    return render_to_response('edit.html', {'task': task}, RequestContext(request))

def postpone(request, list_id, series_id, task_id):
    task = database.get_task(list_id, series_id, task_id)
    task.postpone()
    return redirect('home')

def complete(request, list_id, series_id, task_id):
    task = database.get_task(list_id, series_id, task_id)
    task.complete()
    return redirect('home')

def diff_day(request, sign):
    if "date" in request.session:
        date = request.session["date"]
    else:
        date = datetime.date.today()

    request.session["date"] = date + datetime.timedelta(days = sign)

    return redirect('home')

def today(request):
    request.session["date"] = datetime.date.today()
    return redirect('home')

def prev_day(request):
    return diff_day(request, -1)

def next_day(request):
    return diff_day(request, 1)

