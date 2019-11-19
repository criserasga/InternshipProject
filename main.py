import config
import pickle
import os
from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools


def calendarAuth():
    authorization = auth('calendar')
    createEvent(authorization)

def driveAuth():
    authorization = auth('drive')
    createFile(authorization)

#
# DATE & TIME VARIABLES
#
eventSum = 'Dinner with friends'    #placeholder
startDate = '2019-11-15'            #placeholder
endDate = '2019-11-15'              #placeholder
startTime = '19:00'                 #placeholder
endTime = '22:00'                   #placeholder
gmtOffset = '-7:00'                 # for GMT-7 or MDT

    # TODO LIST:
    #   - full string format: 'YYYY-MM-DD' + 'T' + 'HH:MM:SS'
    #   - 'start' and 'end' variables are to be user-input from Django form
    #   - 'Time' forms will autocorrect from single digit (eg. '9') to full length (eg. 09:00)
    #   - 'Date' forms will be input as format requires until string parsing and reordering can be bothered
    #   - for Google Calendar
    #       - always add on another ':00' for 'seconds'
    #       - add '12:00' if PM
    #   - for Google Drive
    #       - create new folder for events
    #       - parse 'startDate' for month, and create new month folder as necessary
    #       - create new files in Drive without having to keep them on local storage


# 
# NAME:     auth
# PURPOSE:  Grants authorization tokens toward Google APIs 
# 
def auth(service):
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('googleToken.pickle'):
        with open('googleToken.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', config.SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('googleToken.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return discovery.build(service, 'v3', http=creds.authorize(Http())))

# 
# NAME:     createEvent
# PURPOSE:  Creates a Google Calendar event from user's input
# 
def createEvent(CALENDAR):
    EVENT = {
        'summary': eventSum,
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


def createFolder(DRIVE):

def createFiles(DRIVE):
