# 
# This file contains all functions necessary for Google's Drive API
# 

from . import main

# 
# LOCAL VARIABLES:
# 
folder_id = ''
fileName = ''
mimeType = 'application/vnd.google-apps.document'
file_queue = []

# 
# NAME:     createFolder
# PURPOSE:  Creates a Google Drive folder from user's input
# 
def createFolder(DRIVE):
    folder_metadata = {
        'name': main.eventName,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    file = DRIVE.files().create(body=folder_metadata, fields='id').execute()
    global folder_id
    folder_id = file.get('id')

# 
# NAME:     createFile
# PURPOSE:  Builds a .txt file of whatever document is needed
# 
def createFile(fileName, docType):
    with open(fileName, 'w+') as file_handler:
        if docType == 'Sales Sheet':
            file_handler.write(
                'Sales Sheet\n'
                'Today\'s Date:\t%s\n\n' % main.notesDate +
                'Event Informaion:\n'
                '\tName:\t%s\n' % main.eventName +
                '\tDate:\t%s\n' % main.eventDate +
                '\tType:\t%s\n' % main.eventType +
                '\tTime:\t%s\n' % main.eventTime +
                '\t\tEarliest Setup:\t%s\n' % main.eventSetup +
                '\t\tLatest Takedown:\t%s\n' % main.eventTakedown +
                '\tLocation:\t%s\n\n' % main.eventLocation +
                'Informatino for Us:\n'
                '\tDress Code:\t%s\n' % main.eventDress +
                '\tWi-Fi Availability:\t\n'
                '\tDJ Requested:\t\n'
                '\tMusic Type:\t%s\n' % main.eventMusic +
                '\tLighting:\t\n'
                '\tNext Steps:\t%s\n' % main.notesNext +
                '\tAdditional Notes:\t%s\n\n' % main.notesNotes +
                'Sales Rep:\t%s' % main.notesRep
            )
        if docType == 'Event Sheet':
            file_handler.write(
                'Event Sheet\n\n'
                'Event Details:\n'
                '\tName:\t%s\n' % main.eventName +
                '\tDate:\t%s\n' % main.eventDate +
                '\tLocation/Address:\t%s\n' % main.eventLocation +
                '\tScheduled Times:\t%s-%s\n\n' % (main.startTime, main.endTime) +
                'Sales Rep:\t%s\n' % main.notesRep +
                'Event Lead:\t\n'
                'Other Staff:\t\n'
                'Setup Time:\t%s\n' % main.eventSetup +
                'Takedown Time:\t%s\n' % main.eventTakedown +
                'Point of Contact:\t%s\n%s\n' % (main.clientName, main.clientPhone) + 
                'Vehicle:\t\n'
                '\tAnticipated Miles:\t\n'
                'Dress Code:\t%s\n' % main.eventDress +
                'Invoice Number:\t%s\n\n' % main.notesInv +
                'Staff Notes:\t%s' % main.notesNotes
            )
        # if docType == 'Pack List'
        # if docType == 'Contract'

# 
# NAME:     queueFiles
# PURPOSE:  Adds files to an array queue to be uploaded
# 
def queueFile(DRIVE, docType):
    temp_list = []
    fileName = '%s %s.txt' % (main.eventName, docType)
    createFile(fileName, docType)
    temp_list.append(fileName)
    temp_list.append(mimeType)
    file_metadata = tuple(temp_list)
    file_queue.append(file_metadata)

# 
# NAME:     uploadFiles
# PURPOSE:  Uploads files into their parent folder
# 
def moveFiles(DRIVE):
    for filename, mimeType in file_queue:
        metadata = {
            'name': filename,
            'parents': [folder_id]
            }
    if mimeType:
        metadata['mimeType'] = mimeType
    result = DRIVE.files().create(body=metadata, media_body=filename).execute()