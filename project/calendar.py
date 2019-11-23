# 
# This file contains all functions necessary for Google's Calendar API
# 

# TODO List:
# - always add on another ':00' for 'seconds'
# - add '12:00' if PM

# 
# NAME:     createEvent
# PURPOSE:  Creates a Google Calendar event from user's input
# 
def createEvent(CALENDAR):
    EVENT = {
        'summary': eventName,
        'start':  {'dateTime': startDate + 'T' + startTime + '%s' % gmtOffset},
        'end':    {'dateTime': endDate + 'T' + endTime + '%s' % gmtOffset},
        'attendees': [
            #{'email': 'friend1@example.com'},
            #{'email': 'friend2@example.com'},
        ],
    }

    # The entire calendar build request
    e = CALENDAR.events().insert(calendarId='primary',
        sendNotifications=True, body=EVENT).execute()

    # Check to see what it entered into the calendar
    print('''*** %r event added:
    Start: %s
    End:   %s''' % (e['summary'].encode('utf-8'),
        e['start']['dateTime'], e['end']['dateTime']))