# 
# This file contains all webpage (views) render definitions
# 

from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from .forms import SalesSheet
from . import main

def sales_sheet(request):
    form = SalesSheet(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            # Client Variables
            main.clientName = form.cleaned_data.get('client_name')
            main.clientPhone = form.cleaned_data.get('client_phone')
            main.clientEmail = form.cleaned_data.get('client_email')
            main.clientCompany = form.cleaned_data.get('client_company')

            # Event Variables
            main.eventName = form.cleaned_data.get('event_name')
            main.eventType = form.cleaned_data.get('event_type')
            main.eventDate = form.cleaned_data.get('event_date')
            main.eventTime = form.cleaned_data.get('event_time')
            main.eventEnd = form.cleaned_data.get('event_end')
            main.eventSetup = form.cleaned_data.get('event_setup')
            main.eventTakedown = form.cleaned_data.get('event_takedown')
            main.eventLocation = form.cleaned_data.get('event_location')
            main.eventDress = form.cleaned_data.get('event_dress')
            main.eventMusic = form.cleaned_data.get('event_music')
            
            # Notes Variables
            main.notesRep = form.cleaned_data.get('notes_rep')
            main.notesInv = form.cleaned_data.get('notes_inv')
            main.notesDate = form.cleaned_data.get('notes_date')
            main.notesNext = form.cleaned_data.get('notes_next')
            main.notesNotes = form.cleaned_data.get('notes_notes')

            # Calendar-Specific Variables
            main.startDate = main.eventDate
            main.endDate = main.startDate
            main.startTime = main.eventTime
            main.endTime = main.eventEnd

            # Make things work
            main.drive()
            main.calendar()
            return redirect('submit')
    else:
        return render(request, "project/form.html", {'form': form})

def submit(request):
    return render(request, 'project/submit.html')