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
                'Today\'s Date:\t\n\n'
                'Event Informaion:\n'
                '\tName:\t\n'
                '\tDate:\t\n'
                '\tType:\t\n'
                '\tTime:\t\n'
                '\t\tEarliest Setup:\t\n'
                '\t\tLatest Takedown:\t\n'
                '\tLocation:\t\n\n'
                'Informatino for Us:\n'
                '\tDress Code:\t\n'
                '\tWi-Fi Availability:\t\n'
                '\tDJ Requested:\t\n'
                '\tMusic Type:\t\n'
                '\tLighting:\t\n'
                '\tNext Steps:\t\n'
                '\tAdditional Notes:\t\n\n'
                'Sales Rep:\t'
            )
        if docType == 'Event Sheet':
            file_handler.write(
                'Event Sheet\n\n'
                'Event Details:\n'
                '\tName:\t\n'
                '\tDate:\t\n'
                '\tLocation/Address:\t\n'
                '\tScheduled Times:\t\n\n'
                'Sales Rep:\t\n'
                'Event Lead:\t\n'
                'Other Staff:\t\n'
                'Setup Time:\t\n'
                'Takedown Time:\t\n'
                'Point of Contact:\t\n'
                'Vehicle:\t\n'
                '\tAnticipated Miles:\t\n'
                'Dress Code:\t\n'
                'Invoice Number:\t\n\n'
                'Staff Notes:\t'
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