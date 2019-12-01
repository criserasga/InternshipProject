# 
# This file contains all forms used
# 

from django import forms

class SalesSheet(forms.Form):
    client_name = forms.CharField(label='Client Name')
    client_phone = forms.CharField(label='Client Phone Number')
    client_email = forms.EmailField(label='Client E-Mail')
    client_company = forms.CharField(label='Client Organization/Company')
    
    event_name = forms.CharField(label='Event Name')
    event_type = forms.CharField(label='Event Type')
    event_sponsor = forms.BooleanField(label='Sponsorship', 
        help_text='Are we sponsors for this event?', required=False)
    event_date = forms.DateField(label='Event Date', 
        input_formats=['%Y-%m-%d'], help_text='YYYY-MM-DD')
    event_time = forms.TimeField(label='Event Time', 
        input_formats=['%H:%M'], help_text='HH:MM')
    event_end = forms.TimeField(label='Event End Time', 
        input_formats=['%H:%M'], help_text='HH:MM')
    event_setup = forms.TimeField(label='Earliest Setup Time', 
        help_text='When is the earliest we can come in for setup?', input_formats=['%H:%M'], required=False)
    event_takedown = forms.TimeField(label='Latest Takedown Time', 
        help_text='When is the latest we have to be out for takedown?', input_formats=['%H:%M'], required=False)
    event_location = forms.CharField(label='Event Location')
    event_dress = forms.CharField(label='Event Dress Code', 
        help_text='How well should we dress for the event?')
    event_wifi = forms.BooleanField(label='Wi-Fi',
        help_text='Is Wi-Fi available to us?', required=False)
    event_dj = forms.BooleanField(label='DJ Requested', 
        help_text='Is a DJ needed for this event?', required=False)
    event_music = forms.CharField(label='Music Type', 
        help_text='What kind of music does the event need?', required=False)
    event_lights = forms.BooleanField(label='Event Lighting', 
        help_text='Do we need to bring lighting at the event?', required=False)
    
    notes_rep = forms.CharField(label='Sales Rep', 
        help_text='Who made the sale?')
    notes_inv = forms.IntegerField(label='Estimate/Invoice Number')
    notes_date = forms.DateField(label='Today\'s Date', 
        input_formats=['%Y-%m-%d'])
    notes_next = forms.CharField(label='Next Step', 
        help_text='What is the next step for this client?', required=False)
    notes_notes = forms.CharField(label='Additional Notes', 
        widget=forms.Textarea, required=False)