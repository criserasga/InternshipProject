# 
# These are all the forms used in the Sales Sheet
# 
from django import forms

class EventForm(form.Form):
    event_name = forms.CharField(label='Event Name')
    event_type = forms.CharField(label='Event Type')
    event_sponsor = forms.BooleanField('Sponsorship', 
        help_text='Are we sponsors for this event?')
    event_date = forms.DateField(label='Event Date')
    event_time = forms.TimeField(label='Event Time')
    event_duration = forms.DurationField(label='Event Duration', 
        help_text='How long is the event running for?')
    event_setup = forms.TimeField(label='Earliest Setup Time', 
        help_text='When is the earliest we can come in for setup?')
    event_takedown = forms.TimeField(label='Latest Takedown Time', 
        help_text='When is the latest we have to be out for takedown?')
    event_location = forms.CharField(label='Event Location')
    event_dress = forms.CharField(label='Event Dress Code', 
        help_text='What is the dress code for the event?')
    event_wifi = forms.BooleanField(label='Is Wi-Fi available to us?')
    event_dj = forms.BooleanField(label='DJ Requested', 
        help_text='Is a DJ needed for this event?')
    event_music = forms.CharField(label='Music Type', 
        help_text='What kind of music does the event need')
    event_lights = forms.BooleanField(label='Event Lighting', 
        help_text='Do we need to bring lighting at the event?')

class ClientForm(form.Form):
    client_name = forms.CharField(label='Client Name')
    #client_phone = 
    client_email = forms.EmailField(label='Client E-Mail')
    client_company = forms.CharField(lable='Client Organization/Company')

class NotesForm(form.Form):
    notes_sales = forms.CharField(label='Sales Rep', 
        help_text='Who made the sale?')
    notes_invoice = forms.PositiveIntegerField(label='Estimate/Invoice Number')
    notes_date = forms.DateField.auto_now
    notes_next = forms.CharField(label='Next Step', 
        help_text='What is the next step for this client?')
    notes_notes = forms.TextField(label='Additional Notes')

#class PackagesForm(form.Form)