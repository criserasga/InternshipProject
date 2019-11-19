import config
import pickle
import os
from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

def auth():
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
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('googleToken.pickle', 'wb') as token:
            pickle.dump(creds, token)

    CALENDAR = discovery.build('calendar', 'v3', http=creds.authorize(Http()))
    DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

# 
# NAME:     createEvent
# PURPOSE:  Creates a Google Calendar event from user's input
# 
def createEvent():
    EVENT = {
        'summary': config.eventSum,
        'start':  {'dateTime': config.startDate + 'T' + config.startTime + '%s' % config.gmtOffset},
        'end':    {'dateTime': config.endDate + 'T' + config.endTime + '%s' % config.gmtOffset},
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


def createFolder():

def createDocs():

def uploadDocs():