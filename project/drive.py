# 
# This file contains all functions necessary for Google's Drive API
# 

# TODO List:
# - create new folder for events
# - parse 'startDate' for month, and create new month folder as necessary
# - create new files in Drive without having to keep them on local storage

# 
# LOCAL VARIABLES:
# 
folder_id = ''
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
# NAME:     queueFiles
# PURPOSE:  Adds files to an array queue to be uploaded
# 
def queueFiles(DRIVE, docType):
    temp_list = []
    temp_str = main.eventName + ' ' + docType
    temp_list.append(temp_str)
    temp_list.append(mimeType)
    file_metadata = tuple(temp_list)
    file_queue.append(file_metadata)

# 
# NAME:     uploadFiles
# PURPOSE:  Uploads files into their parent folder
# 
def moveFiles():
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