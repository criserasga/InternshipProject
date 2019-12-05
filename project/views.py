# 
# This file contains all webpage (views) render definitions
# 

from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from .forms import SalesSheet
from .forms import CHOICES
from .forms import PACKAGES
from . import main

# dictionary of packages
#packages = {
#    "go big or go home": "700 vertek 5000w\nsmall 200w sub",
#    "next package": "stuf"
#}

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
            main.eventSponsor = form.cleaned_data.get('event_sponsor')
            if main.eventSponsor == True:
                main.eventSponsor = 'Yes'
            else:
                main.eventSponsor = 'No'
            main.eventDate = form.cleaned_data.get('event_date')
            main.eventTime = form.cleaned_data.get('event_time')
            main.eventEnd = form.cleaned_data.get('event_end')
            main.eventSetup = form.cleaned_data.get('event_setup')
            main.eventTakedown = form.cleaned_data.get('event_takedown')
            main.eventLocation = form.cleaned_data.get('event_location')
            main.eventDress = form.cleaned_data.get('event_dress')
            main.eventWifi = form.cleaned_data.get('event_wifi')
            if main.eventWifi == True:
                main.eventWifi = 'Yes'
            else:
                main.eventWifi = 'No'
            main.eventDj = form.cleaned_data.get('event_dj')
            if main.eventDj == True:
                main.eventDj = 'Yes'
            else:
                main.eventDj = 'No'
            main.eventMusic = form.cleaned_data.get('event_music')
            main.eventLights = form.cleaned_data.get('event_lights')
            if main.eventLights == True:
                main.eventLights = 'Yes'
            else:
                main.eventLights = 'No'
            
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

            # Equipment Variables
            main.packageName = CHOICES[int(form.cleaned_data.get('package_choice'))]
            main.packageName = main.packageName[1]
            main.packageChoice = PACKAGES[(int(form.cleaned_data.get('package_choice'))-1)]

            # Make things work
            main.drive()
            main.calendar()
            return redirect('submit')
    else:
        return render(request, "project/form.html", {'form': form})

def submit(request):
    return render(request, 'project/submit.html')