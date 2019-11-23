# 
# This file contains all functions necessary for Google's Drive API
# 

# TODO List:
# - create new folder for events
# - parse 'startDate' for month, and create new month folder as necessary
# - create new files in Drive without having to keep them on local storage

# 
# NAME:     createFolder
# PURPOSE:  Creates a Google Drive folder from user's input
# 
def createFolder(DRIVE):
    file_metadata = {
    'name': eventName,
    'mimeType': 'application/vnd.google-apps.folder'
    }
    file = DRIVE.files().create(body=file_metadata, fields='id').execute()
    folderId = file.get('id')

# 
# NAME:     createFolder
# PURPOSE:  Creates files from user's input
# 
def createFiles(DRIVE):
    file_metadata = {
        'name': eventName,
        'parents': folderId
    }
