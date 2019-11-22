from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from . import forms

def sales_sheet(request):
    event_form = EventForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
#            main.eventName = 
#            main.startDate = 
#            main.end
            return

    else:
        return render(request, "project/form.html", {'event_form': form})