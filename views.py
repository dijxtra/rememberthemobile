from datetime import datetime, date
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
import datetime
import database

def index(request, date = None):
    if date is None:
        if "date" in request.session:
            date = request.session["date"]
        else:
            date = datetime.date.today()
            
    tasks = database.get_date(date.strftime("%Y-%m-%d"))

    tasks = sorted(tasks, key = lambda task: task.priority())
    
    head_days = ['today', '&larr;', date.strftime("%Y-%m-%d"), '&rarr;']

    request.session["date"] = date
    
    d = {'tasks': tasks, 'head_days': head_days}
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

def edit(request, id):
    return render_to_response('edit.html', {'id': id}, RequestContext(request))

def postpone(request, id):
    return index(request)

def complete(request, id):
    return index(request)

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

