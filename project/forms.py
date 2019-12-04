# 
# This file contains all forms used
# 

from django import forms

PACKAGES = [
    'x1 Speaker\nx1 Speaker Stand\nx1 Wired Mic\nx1 8-Channel Mixer\nNecessary Cables and Small Cable Tote',
    'x2 Speakers\nx2 Speaker Stands\nx1 Wireless Mic\nx1 Wired Mic\nx1 8-Channel Mixer\nNecessary Cables and Small Cable Tote',
    'x3 Speakers\nx3 Speaker Stands\nx2 Wireless Mics\nx1 Wired Mic\nx1 Ui24R\nx1 iPad\nNecessary Cables and Medium/Large Cable Tote',
    'x3 Speakers\nx3 Speaker Stands\nx2 Wireless Mics\nx1 Wired Mic\nx1 Lavalier\nx1 Ui24R\nx1 iPad\nNecessary Cables and Medium/Large Cable Tote',
    'x4 Speakers\nx4 Speaker Stands\nx2 Wireless Mics\nx1 Ui24R Mixer\nx1 iPad\nNecessary Cables and Medium/Large Cable Tote',
    'x4 Speakers\nx4 Speaker Stands\nx2 Wireless Mics\nx1 Lavalier\nx1 Ui24R\nx1 iPad\nNecessary Cables and Medium/Large Cable Tote',
    'x2-x4 VRX Speakers\nx1-x2 Subwoofer(s)\nx2 Speaker Stands\nx4-x6 Wireless Mics\nx1 Amp Rack\nx1 Ui24R (or SQ-6)\nSpeakon Cable Tote',
    'x1 DJ Controller\nx1 Wireless Mic',
    'x2 70" TVs\nx2 TV Frames\nx2 8\' Truss\nx2 Flat Baseplates\nx1 Laptop\n1 Presentation Clicker\nHDMI Tote\nPins Ammo Case\nBrass Hammers',
    'x2 70" TVs\nx2 TV Frames\nx2 8\' Truss\nx1 32" TV\nx2 Flat Baseplates\nx1 Laptop\n1 Presentation Clicker\nHDMI Tote\nPins Ammo Case\nBrass Hammers',
    'x3 70" TVs\nx3 TV Frames\nx3 8\' Truss\nx3 Flat Baseplates\nx1 Laptop\n1 Presentation Clicker\nHDMI Tote\nPins Ammo Case\nBrass Hammers',
    'x3 70" TVs\nx3 TV Frames\nx3 8\' Truss\nx1 32" TV\nx3 Flat Baseplates\nx1 Laptop\n1 Presentation Clicker\nHDMI Tote\nPins Ammo Case\nBrass Hammers',
    'x4 70" TVs\nx4 TV Frames\nx4 8\' Truss\nx4 Flat Baseplates\nx1 Laptop\n1 Presentation Clicker\nHDMI Tote\nPins Ammo Case\nBrass Hammers',
    'x4 70" TVs\nx4 TV Frames\nx4 8\' Truss\nx1 32" TV\nx4 Flat Baseplates\nx1 Laptop\n1 Presentation Clicker\nHDMI Tote\nPins Ammo Case\nBrass Hammers',
    'x4 SDI Cables\nBlack Magic Adapters',
    'x2 Speakers\nx2 Speaker Stands\nx2 Wireless Mics\nx1 Computer\nPresentation Clicker\nx1 10\' Screen\nx1 Projector\nx1 Ui24R\nx1 iPad\nNecessary Cables',
    'x2 Speakers\nx2 Speaker Stands\nx4 Wireless Mics\nx4 Moving Heads\nx4 LED Par Cans\nx1 Computer\nx1 Presentation Clicker\nx1 14\' Screen\nx1 Projector\nx1 Ui24R\nx1 iPad\nNecessary Cables',
    'x4 Speakers\nx4 Speaker Stands\nx1 Subwoofer\nx8 Wireless Mics\nx8 Moving Heads\nx8 LED Par Cans\nx9 Stage Decks\nx36 2\' Stage Legs\nx1 2\' Stage Stairs\nx20 Carpet Squares\nx2 Computers\nx1 Presentation Clicker\nx2 14\' Screens\nx2 Projectors\nx1 SQ-6\nStage Skirt\nNecessary Cables',
    'x6 Speakers\nx6 Speaker Stands\nx2 Subwoofers\nx10 Wireless Mics\nx12 Moving Heads\nx12 LED Par Cans\nx24 Stage Decks\nx28 4\' Stage Frames\nx24 Short Frame Bars\nx24 Long Frame Bars\nx4 Single Nipples\nx16 Double Nipples\nx15 Quad Nipples\nx1 4\' Stage Stairs\nx37 Carpet Squares\nx2 Computers\nx1 Presentation Clicker\nx2 14\' Screens\nx2 Projectors\nx1 SQ-6\nStage Skirt\nNecessary Cables',
    'x2 Speakers\nx2 Speaker Stands\nx1 Wireless Mic\nx1 10\' Screen\nx1 Projector\nx1 Computer\nx1 Presentation Clicker\nx1 Mixer\nNecessary Cables',
    'x2 Speakers\nx2 Speaker Stands\nx4 Uplights\nx1 Wireless Mic\nx1 Lavalier\nx1 Ui24R\nx1 iPad\nx1 DJ Controller\nx2 70" TVs\nx2 TV Frames\nx2 8\' Truss\nx1 32" TV\nx2 Flat Baseplates\nx1 Laptop\n1 Presentation Clicker\nHDMI Tote\nNecessary Cables\nPins Ammo Case\nBrass Hammers',
    'x4 Speakers\nx4 Speaker Stands\nx6 Uplights\nx2 Wireless Mics\nx2 Lavaliers\nx1 Ui24R\nx1 iPad\nx1 Tascam\nx1 DJ Controller\nx2 70" TVs\nx2 TV Frames\nx2 8\' Truss\nx1 32" TV\nx2 Flat Baseplates\nx1 Laptop\n1 Presentation Clicker\nHDMI Tote\nNecessary Cables\nPins Ammo Case\nBrass Hammers',
    'x2 Speakers\nx2 Speaker Stands\nx1 Wireless Mic\nx1 DJ Controller\nNecessary Cables and Small Cable Tote',
    'x2 Speakers\nx2 Speaker Stands\nx1 Single 18" Subwoofer\nx1 Wireless Mic\nx1 DJ Controller\nNecessary Cables and Small Cable Tote',
    'x2 Speakers\nx2 Speaker Stands\nx1 Double 18" Subwoofer\nx1 Wireless Mic\nx1 DJ Controller\nx4 LED Par Cans\nx1 Lighting Controller\nx3 10\' Truss\nx2 X-plates\nx8 Carpet Squares\nDMX Tote\nNecessary Cables and Small Cable Tote',
    'x2 Speakers\nx2 Speaker Stands\nx1 Double 18" Subwoofer\nx2 Wireless Mics\nx1 DJ Controller\nx2 Moving Heads\nx8 LED Par Cans\nx1 Lighting Controller\nx4 10\' Truss\nx2 X-plates\nx2 Stage Decks\nx8 2\' Stage Legs\nx1 2\' Stage Stairs\nx18 Carpet Squares\nStage Skirt\nDMX Tote\nNecessary Cables and Large Cable Tote',
    'x2 QSC Speakers\nx2 Speaker Stands\nx1 Double 18" Subwoofer\nx2 Wireless Mics\nx1 DJ Controller\nx2 Lasers\nx6 Moving Heads\nx12 LED Par Cans\nx1 Fog Machine\nx1 Lighting Controller\nx4 10\' Truss\nx2 X-plates\nx2 Stage Decks\nx8 2\' Stage Legs\nx1 2\' Stage Stairs\nx18 Carpet Squares\nStage Skirt\nDMX Tote\nNecessary Cables and Large Cable Tote',
    'x4 VRX Speakers\nx2 Speaker Stands\nx2 Passive Double 18" Subwoofers\nx1 Amp Rack\nx2 Wireless Mics\nx1 DJ Controller\nx2 Lasers\nx6 Moving Heads\nx12 LED Par Cans\nx1 Fog Machine\nx1 Lighting Controller\nx4 10\' Truss\nx2 X-plates\nx2 Stage Decks\nx8 2\' Stage Legs\nx1 2\' Stage Stairs\nx18 Carpet Squares\nStage Skirt\nDMX Tote\nNecessary Cables and Large Cable Tote',
    'x2 Speakers\nx2 Speaker Stands\nx1 Wireless Mic\nx1 DJ Controller\n Necessary Cables and Small Cable Tote',
    'x2 Speakers\nx2 Speaker Stands\nx1 Single 18" Subwoofer\nx1 Wireless Mic\nx1 Lavalier\nx1 DJ Controller\n Necessary Cables and Small Cable Tote',
    'x4 Speakers\nx4 Speaker Stands\nx1 Double 18" Subwoofer\nx1 Wireless Mic\nx1 Lavalier\nx1 DJ Controller\n Necessary Cables and Large Cable Tote',
]

CHOICES = [
    (0, '-- Select One --'),
    (1, '1 Speaker Package'),
    (2, '2 Speaker Package'),
    (2, '3 Speaker Package'),
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

    package_choice = forms.ChoiceField(label='Select Event Package', 
        widget=forms.Select, required=False, choices=CHOICES)
