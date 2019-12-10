# 
# This file contains all functions necessary for Google's Calendar API
# 

from . import main

# 
# NAME:     createEvent
# PURPOSE:  Creates a Google Calendar event from user's input
# 
def createEvent(CALENDAR):
    EVENT = {
        'summary': main.eventName,
        'location': main.eventLocation,
        'description': 'A(n) %s for %s, of %s.' % (main.eventType, main.clientName, main.clientCompany),
        'start':  {'dateTime': '%sT%s%s' % (main.startDate, main.startTime, main.gmtOffset)},
        'end':    {'dateTime': '%sT%s%s' % (main.endDate, main.endTime, main.gmtOffset)},
    }
    
    def calendarType():
        if main.eventType == 'Rental':
            return 'andx.us_96tc1dm6kd2a290gf7bjctjors@group.calendar.google.com'
        else:
            return 'sjci8ir4pifr9mskkrnev28q6s@group.calendar.google.com'

    # The entire calendar build request
    e = CALENDAR.events().insert(calendarId=calendarType(),
        sendNotifications=True, body=EVENT).execute()