from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from . import config
from . import drive
from .drive import createFolder
from .drive import queueFile
from .drive import moveFiles
from .calendar import createEvent
from .gmail import CreateMessage
from .gmail import SendMessage
from . import calendar
import pickle
import os


# 
# CLIENT VARIABLES
# 
clientName = None
clientPhone = None
clientEmail = None
clientCompany = None

#
# EVENT VARIABLES
#
eventName = None
eventType = None
eventSponsor = None
eventDate = None
eventTime = None
eventEnd = None
eventSetup = None
eventTakedown = None
eventLocation = None
eventDress = None
eventWifi = None
eventDj = None
eventMusic = None
eventLights = None

# 
# NOTES VARIABLES
# 
notesRep = None
notesInv = None
notesDate = None
notesNext = None
notesNotes = None

# 
# EQUIPMENT VARIABLES
# 
packageName = None
packageChoice = None

# 
# CALENDAR-SPECIFIC VARIABLES
# 
startDate = None
endDate = None
startTime = None
endTime = None
gmtOffset = '-07:00'    # for GMT-7 or MDT

# 
# DRIVE-SPECIFIC VARIABLES
# 
folderId = None

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

    if service == 'gmail':
        authentication = build(service, 'v1', credentials=creds)
    else:
        authentication = build(service, 'v3', credentials=creds)
    
    return authentication


def calendar():
    authorization = auth('calendar')
    createEvent(authorization)

def drive():
    authorization = auth('drive')
    createFolder(authorization)
    queueFile(authorization, 'Sales Sheet')
    queueFile(authorization, 'Event Sheet')
    queueFile(authorization, 'Pack List')
    queueFile(authorization, 'Contract')
    moveFiles(authorization)

def mail():
    authorization = auth('gmail')
    message = CreateMessage('cris@andx.us, mcerasga@hotmail.com', 'cris@andx.us', 'A new event was created', 'Please review the event documents here:\nhttps://drive.google.com/drive/folders/%s' % folderId)
    SendMessage(authorization, 'me', message)