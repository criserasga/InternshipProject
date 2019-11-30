# 
# This file contains all functions necessary for Google's Drive API
# 

from . import main


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
                'Name:\t\n'
                'Date:\t\n'
                'Type:\t\n'
                'Time:\t\n'
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