from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from .forms import EventForm
from .forms import ClientForm
from .forms import NotesForm

# TODO: figure out how to render multiple forms on one page under one submit button

def sales_sheet(request):
    client_form = ClientForm(request.POST or None)
    event_form = EventForm(request.POST or None)
    notes_form = NotesForm(request.POST or None)

    if request.method == "POST":
        if event_form.is_valid():
            return
    else:
        return render(request, "project/form.html", {'event_form': event_form})