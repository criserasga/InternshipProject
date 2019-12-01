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
            main.eventName = form.cleaned_data.get('event_name')
            main.startDate = form.cleaned_data.get('event_date')
            main.endDate = main.startDate
            main.startTime = form.cleaned_data.get('event_time')
            main.endTime = form.cleaned_data.get('event_end')

            main.drive()
            main.calendar()
            return redirect('submit')
    else:
        return render(request, "project/form.html", {'form': form})

def submit(request):
    return render(request, 'project/submit.html')