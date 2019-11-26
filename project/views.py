# 
# This file contains all webpage (views) render definitions
# 

from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from .forms import EventForm
from .forms import ClientForm
from .forms import NotesForm

# TODO: 
# - assign input data into MAIN.PY variables
# - render multiple forms on one page 
# - submit multiple forms under one submit button

def sales_sheet(request):
    client_form = ClientForm(request.POST or None)
    event_form = EventForm(request.POST or None)
    notes_form = NotesForm(request.POST or None)

    if request.method == "POST":
        if client_form.is_valid():
            return
    else:
        return render(request, "project/form.html", {'client_form': client_form})