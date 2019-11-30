# 
# This file contains all webpage (views) render definitions
# 

from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from .forms import EventForm
from .forms import ClientForm
from .forms import NotesForm
from . import main


def sales_sheet(request):
    # client_form = ClientForm(request.POST or None)
    event_form = EventForm(request.POST or None)
    # notes_form = NotesForm(request.POST or None)

    if request.method == "POST":
        if event_form.is_valid():
            main.eventName = event_form.cleaned_data.get('event_name')
            main.startDate = event_form.cleaned_data.get('event_date')
            main.endDate = main.startDate
            main.startTime = event_form.cleaned_data.get('event_time')
            # main.endTime = 

            
            main.drive()
            main.calendar()
            # # test prints to see if variables are assigned
            # print('Event Name: %s' % (main.eventName))
            # print('Event Date: %s' % (main.startDate))
            # print('Event Time: %s' % (main.startTime))
            return redirect('submit')
    else:
        return render(request, "project/form.html", {'event_form': event_form})

def submit(request):
    return render(request, 'project/submit.html')