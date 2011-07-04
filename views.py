from datetime import datetime, date
from django.shortcuts import render_to_response
from django.template import RequestContext
import database

def index(request):
    tasks = database.get()
    
    head_days = ['&larr;', 'Today', '&rarr;']
    
    d = {'tasks': tasks, 'head_days': head_days}
    return render_to_response('index.html', d, RequestContext(request))

def edit(request, id):
    task = database.get(id)
    
    d = {'task': task}
    return render_to_response('edit.html', d, RequestContext(request))

def postpone(request, id):
    return index(request)

def complete(request, id):
    return index(request)

def prev_day(request, id):
    return index(request)

def next_day(request, id):
    return index(request)

