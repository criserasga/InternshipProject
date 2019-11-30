# 
# This file contains all functions necessary for Google's Drive API
# 

from . import main

# TODO List:
# - find a way to extract all form data to .txt file
# - connect drive.py to main.py and form
# - create new files in Drive without having to keep them on local storage
# - Files process
#   - form data assigned to main.py variables
#   - main.py variables to .txt/.gdoc
#   - .txt/.gdoc to local storage temporary files
#   - local storage temporary files to Drive
#   - delete local storage temporary files

# 
# LOCAL VARIABLES:
# 
folder_id = ''
fileName = ''
mimeType = None
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
    folder_id = file.get('id')

# 
# NAME:     createFile
# PURPOSE:  Builds a .txt file of whatever document is needed
# 
def createFile(docType):
    with open(fileName, 'w+') as file_handler:
        if docType == 'Sales Sheet':
            file_handler.write(
                'Sales Sheet\n'
                'Today\'s Date:\t\n\n'
                'Event Informaion:\n'
                'Name:\t%s\n' % (main.eventName)
                'Date:\t%s\n' % (main.startDate)
                'Type:\t\n'
                'Time:\t%s\n' % (main.startTime)
                '\tEarliest Setup:\t\n'
                '\tLatest Takedown:\t\n'
                'Location:\t\n'
                'Dress Code:\t\n'
                'Wi-Fi Availability:\t\n'
                'DJ Requested:\t\n'
                'Music Type:\t\n'
                'Lighting:\t\n'
                'Next Steps:\t\n'
                'Additional Notes:\t\n\n'
                'Sales Rep:\t\n'
            )

# 
# NAME:     queueFiles
# PURPOSE:  Adds files to an array queue to be uploaded
# 
def queueFile(DRIVE, docType):
    temp_list = []
    fileName = main.eventName + ' ' + docType + '.txt'
    createFile(docType)
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
    if result:
        print('Uploaded "%s" (%s)' % (filename, result['mimeType']))