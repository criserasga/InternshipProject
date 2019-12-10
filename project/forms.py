# 
# This file contains all forms used
# 

from django import forms
from datetime import datetime

PACKAGES = [
    'x1\tSpeaker\nx1\tSpeaker Stand\nx1\tWired Mic\nx1\t8-Channel Mixer\nNecessary Cables and Small Cable Tote',
    'x2\tSpeakers\nx2\tSpeaker Stands\nx1\tWireless Mic\nx1\tWired Mic\nx1\t8-Channel Mixer\nNecessary Cables and Small Cable Tote',
    'x3\tSpeakers\nx3\tSpeaker Stands\nx2\tWireless Mics\nx1\tWired Mic\nx1\tUi24R\nx1\tiPad\nNecessary Cables and Medium/Large Cable Tote',
    'x3\tSpeakers\nx3\tSpeaker Stands\nx2\tWireless Mics\nx1\tWired Mic\nx1\tLavalier\nx1\tUi24R\nx1\tiPad\nNecessary Cables and Medium/Large Cable Tote',
    'x4\tSpeakers\nx4\tSpeaker Stands\nx2\tWireless Mics\nx1\tUi24R Mixer\nx1\tiPad\nNecessary Cables and Medium/Large Cable Tote',
    'x4\tSpeakers\nx4\tSpeaker Stands\nx2\tWireless Mics\nx1\tLavalier\nx1\tUi24R\nx1\tiPad\nNecessary Cables and Medium/Large Cable Tote',
    'x2-x4\tVRX Speakers\nx1-x2\tSubwoofer(s)\nx2\tSpeaker Stands\nx4-x6\tWireless Mics\nx1\tAmp Rack\nx1\tUi24R (or SQ-6)\nSpeakon Cable Tote',
    'x1\tDJ Controller\nx1\tWireless Mic',
    'x2\t70" TVs\nx2\tTV Frames\nx2\t8\' Truss\nx2\tFlat Baseplates\nx1\tLaptop\nx1\tPresentation Clicker\nHDMI Tote\nPins Ammo Case\nBrass Hammers',
    'x2\t70" TVs\nx2\tTV Frames\nx2\t8\' Truss\nx1\t32" TV\nx2\tFlat Baseplates\nx1\tLaptop\nx1\tPresentation Clicker\nHDMI Tote\nPins Ammo Case\nBrass Hammers',
    'x3\t70" TVs\nx3\tTV Frames\nx3\t8\' Truss\nx3\tFlat Baseplates\nx1\tLaptop\nx1\tPresentation Clicker\nHDMI Tote\nPins Ammo Case\nBrass Hammers',
    'x3\t70" TVs\nx3\tTV Frames\nx3\t8\' Truss\nx1\t32" TV\nx3\tFlat Baseplates\nx1\tLaptop\nx1\tPresentation Clicker\nHDMI Tote\nPins Ammo Case\nBrass Hammers',
    'x4\t70" TVs\nx4\tTV Frames\nx4\t8\' Truss\nx4\tFlat Baseplates\nx1\tLaptop\nx1\tPresentation Clicker\nHDMI Tote\nPins Ammo Case\nBrass Hammers',
    'x4\t70" TVs\nx4\tTV Frames\nx4\t8\' Truss\nx1\t32" TV\nx4\tFlat Baseplates\nx1\tLaptop\nx1\tPresentation Clicker\nHDMI Tote\nPins Ammo Case\nBrass Hammers',
    'x4\tSDI Cables\nBlack Magic Adapters',
    'x2\tSpeakers\nx2\tSpeaker Stands\nx2\tWireless Mics\nx1\tComputer\nPresentation Clicker\nx1\t10\' Screen\nx1\tProjector\nx1\tUi24R\nx1\tiPad\nNecessary Cables',
    'x2\tSpeakers\nx2\tSpeaker Stands\nx4\tWireless Mics\nx4\tMoving Heads\nx4\tLED Par Cans\nx1\tComputer\nx1\tPresentation Clicker\nx1\t14\' Screen\nx1\tProjector\nx1\tUi24R\nx1\tiPad\nNecessary Cables',
    'x4\tSpeakers\nx4\tSpeaker Stands\nx1\tSubwoofer\nx8\tWireless Mics\nx8\tMoving Heads\nx8\tLED Par Cans\nx9\tStage Decks\nx36\t2\' Stage Legs\nx1\t2\' Stage Stairs\nx20\tCarpet Squares\nx2\tComputers\nx1\tPresentation Clicker\nx2\t14\' Screens\nx2\tProjectors\nx1\tSQ-6\nStage Skirt\nNecessary Cables',
    'x6\tSpeakers\nx6\tSpeaker Stands\nx2\tSubwoofers\nx10\tWireless Mics\nx12\tMoving Heads\nx12\tLED Par Cans\nx24\tStage Decks\nx28\t4\' Stage Frames\nx24\tShort Frame Bars\nx24\tLong Frame Bars\nx4\tSingle Nipples\nx16\tDouble Nipples\nx15\tQuad Nipples\nx1\t4\' Stage Stairs\nx37\tCarpet Squares\nx2\tComputers\nx1\tPresentation Clicker\nx2\t14\' Screens\nx2\tProjectors\nx1\tSQ-6\nStage Skirt\nNecessary Cables',
    'x2\tSpeakers\nx2\tSpeaker Stands\nx1\tWireless Mic\nx1\t10\' Screen\nx1\tProjector\nx1\tComputer\nx1\tPresentation Clicker\nx1\tMixer\nNecessary Cables',
    'x2\tSpeakers\nx2\tSpeaker Stands\nx4\tUplights\nx1\tWireless Mic\nx1\tLavalier\nx1\tUi24R\nx1\tiPad\nx1\tDJ Controller\nx2\t70" TVs\nx2\tTV Frames\nx2\t8\' Truss\nx1\t32" TV\nx2\tFlat Baseplates\nx1\tLaptop\n1 Presentation Clicker\nHDMI Tote\nNecessary Cables\nPins Ammo Case\nBrass Hammers',
    'x4\tSpeakers\nx4\tSpeaker Stands\nx6\tUplights\nx2\tWireless Mics\nx2\tLavaliers\nx1\tUi24R\nx1\tiPad\nx1\tTascam\nx1\tDJ Controller\nx2\t70" TVs\nx2\tTV Frames\nx2\t8\' Truss\nx1\t32" TV\nx2\tFlat Baseplates\nx1\tLaptop\n1 Presentation Clicker\nHDMI Tote\nNecessary Cables\nPins Ammo Case\nBrass Hammers',
    'x2\tSpeakers\nx2\tSpeaker Stands\nx1\tWireless Mic\nx1\tDJ Controller\nNecessary Cables and Small Cable Tote',
    'x2\tSpeakers\nx2\tSpeaker Stands\nx1\tSingle 18" Subwoofer\nx1\tWireless Mic\nx1\tDJ Controller\nNecessary Cables and Small Cable Tote',
    'x2\tSpeakers\nx2\tSpeaker Stands\nx1\tDouble 18" Subwoofer\nx1\tWireless Mic\nx1\tDJ Controller\nx4\tLED Par Cans\nx1\tLighting Controller\nx3\t10\' Truss\nx2\tX-plates\nx8\tCarpet Squares\nDMX Tote\nNecessary Cables and Small Cable Tote',
    'x2\tSpeakers\nx2\tSpeaker Stands\nx1\tDouble 18" Subwoofer\nx2\tWireless Mics\nx1\tDJ Controller\nx2\tMoving Heads\nx8\tLED Par Cans\nx1\tLighting Controller\nx4\t10\' Truss\nx2\tX-plates\nx2\tStage Decks\nx8\t2\' Stage Legs\nx1\t2\' Stage Stairs\nx18\tCarpet Squares\nStage Skirt\nDMX Tote\nNecessary Cables and Large Cable Tote',
    'x2\tQSC Speakers\nx2\tSpeaker Stands\nx1\tDouble 18" Subwoofer\nx2\tWireless Mics\nx1\tDJ Controller\nx2\tLasers\nx6\tMoving Heads\nx12\tLED Par Cans\nx1\tFog Machine\nx1\tLighting Controller\nx4\t10\' Truss\nx2\tX-plates\nx2\tStage Decks\nx8\t2\' Stage Legs\nx1\t2\' Stage Stairs\nx18\tCarpet Squares\nStage Skirt\nDMX Tote\nNecessary Cables and Large Cable Tote',
    'x4\tVRX Speakers\nx2\tSpeaker Stands\nx2\tPassive Double 18" Subwoofers\nx1\tAmp Rack\nx2\tWireless Mics\nx1\tDJ Controller\nx2\tLasers\nx6\tMoving Heads\nx12\tLED Par Cans\nx1\tFog Machine\nx1\tLighting Controller\nx4\t10\' Truss\nx2\tX-plates\nx2\tStage Decks\nx8\t2\' Stage Legs\nx1\t2\' Stage Stairs\nx18\tCarpet Squares\nStage Skirt\nDMX Tote\nNecessary Cables and Large Cable Tote',
    'x2\tSpeakers\nx2\tSpeaker Stands\nx1\tWireless Mic\nx1\tDJ Controller\n Necessary Cables and Small Cable Tote',
    'x2\tSpeakers\nx2\tSpeaker Stands\nx1\tSingle 18" Subwoofer\nx1\tWireless Mic\nx1\tLavalier\nx1\tDJ Controller\n Necessary Cables and Small Cable Tote',
    'x4\tSpeakers\nx4\tSpeaker Stands\nx1\tDouble 18" Subwoofer\nx1\tWireless Mic\nx1\tLavalier\nx1\tDJ Controller\n Necessary Cables and Large Cable Tote',
]

CHOICES = [
    (0, '-- Select One --'),
    (1, '1 Speaker Package'),
    (2, '2 Speaker Package'),
    (3, '3 Speaker Package'),
    (4, '3 Speaker Package w/ Lav'),
    (5, '4 Speaker Package'),
    (6, '4 Speaker Package w/ Lav'),
    (7, 'Passive Audio System'),
    (8, 'Just a DJ'),
    (9, '2 TVs'),
    (10, '2 TVs w/ Presenter View'),
    (11, '3 TVs'),
    (12, '3 TVs w/ Presenter View'),
    (13, '4 TVs'),
    (14, '4 TVs w/ Presenter View'),
    (15, 'SDI TV Package'),
    (16, 'Conference AV Breakout Rooms'),
    (17, 'Conference AV Main Room: LVL 1'),
    (18, 'Conference AV Main Room: LVL 2'),
    (19, 'Conference AV Main Room: LVL 3'),
    (20, 'Corporate AV Package: Basic'),
    (21, 'Corporate AV Package: On Point'),
    (22, 'Corporate AV Package: Step Above'),
    (23, 'DJ Package: Budget Basic'),
    (24, 'DJ Package: Simple Sam'),
    (25, 'DJ Package: Tuesday'),
    (26, 'DJ Package: Kansas'),
    (27, 'DJ Package: Boom'),
    (28, 'DJ Package: Super Nova'),
    (29, 'Wedding Package: Good Time'),
    (29, 'Wedding Package: Remember the Night'),
    (29, 'Wedding Package: Make My Day'),
]

DRESS = [
    (0, '-- Select One --'),
    ('Casual', 'Casual'),
    ('Business Casual', 'Business Casual'),
    ('Formal', 'Formal'),
]

class SalesSheet(forms.Form):
    client_name = forms.CharField(label='Client Name')
    client_phone = forms.CharField(label='Client Phone Number')
    client_email = forms.EmailField(label='Client E-Mail')
    client_company = forms.CharField(label='Client Organization/Company')
    
    event_name = forms.CharField(label='Event Name')
    event_type = forms.CharField(label='Event Type')
    event_sponsor = forms.BooleanField(label='Sponsorship', 
        help_text='Are we sponsoring this event?', required=False)
    event_date = forms.DateField(label='Event Date', 
        input_formats=['%m/%d/%y'])
    event_time = forms.TimeField(label='Start Time', 
        input_formats=['%I:%M %p'])
    event_end = forms.TimeField(label='End Time', 
        input_formats=['%I:%M %p'])
    event_setup = forms.TimeField(label='Earliest Setup Time', 
        input_formats=['%I:%M %p'])
    event_takedown = forms.TimeField(label='Latest Takedown Time', 
        input_formats=['%I:%M %p'])
    event_location = forms.CharField(label='Event Location')
    event_dress = forms.ChoiceField(label='Event Dress Code',
        widget=forms.Select, choices=DRESS)
    event_wifi = forms.BooleanField(label='Wi-Fi',
        help_text='Is Wi-Fi available?', required=False)
    event_dj = forms.BooleanField(label='DJ Requested', 
        help_text='Is a DJ needed?', required=False)
    event_music = forms.CharField(label='Music Type', 
        help_text='What kind of music does the event need?', required=False)
    event_lights = forms.BooleanField(label='Event Lighting', 
        help_text='Do we need to bring lighting?', required=False)
    
    notes_rep = forms.CharField(label='Sales Rep')
    notes_inv = forms.IntegerField(label='Estimate/Invoice Number')
    notes_date = forms.DateField(label='Today\'s Date', 
        input_formats=['%m/%d/%y'])
    notes_next = forms.CharField(label='Next Step', 
        help_text='What is the next step for this client?', required=False)
    notes_notes = forms.CharField(label='Additional Notes', 
        widget=forms.Textarea, required=False)

    package_choice = forms.ChoiceField(label='Select Event Package', 
        widget=forms.Select, required=False, choices=CHOICES)
