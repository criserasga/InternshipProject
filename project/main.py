from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from . import config
import pickle
import os


def calendarAuth():
    authorization = auth('calendar')
    createEvent(authorization)

def driveAuth():
    authorization = auth('drive')
    createFolder(authorization)
    queueFile(authorization, 'Sales Sheet')
    queueFile(authorization, 'Event Sheet')
    queueFile(authorization, 'Pack List')
    queueFile(authorization, 'Contract')
    moveFiles(authorization)


# 
# NAME VARIABLES
# 
eventName = ''

#
# DATE & TIME VARIABLES
#
startDate = ''
endDate = ''
startTime = ''
endTime = ''
gmtOffset = '-7:00'                 # for GMT-7 or MDT

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

    return discovery.build(service, 'v3', http=creds.authorize(Http()))