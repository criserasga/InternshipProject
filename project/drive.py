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
                'Event Information:\n'
                '\tName:\t\t%s\n' % main.eventName +
                '\tDate:\t\t%s\n' % main.eventDate +
                '\tType:\t\t%s\n' % main.eventType +
                '\tTime:\t\t%s\n' % main.eventTime +
                '\t\tEarliest Setup:\t\t%s\n' % main.eventSetup +
                '\t\tLatest Takedown:\t%s\n' % main.eventTakedown +
                '\tLocation:\t%s\n\n' % main.eventLocation +
                'Information for Us:\n'
                '\tSponsorship:\t\t%s\n' % main.eventSponsor +
                '\tDress Code:\t\t%s\n' % main.eventDress +
                '\tWi-Fi Availability:\t%s\n' % main.eventWifi +
                '\tDJ Requested:\t%s\n' % main.eventDj +
                '\tMusic Type:\t\t%s\n' % main.eventMusic +
                '\tLighting:\t\t%s\n' % main.eventLights +
                '\tNext Steps:\t\t%s\n' % main.notesNext +
                '\tAdditional Notes:\t%s\n\n' % main.notesNotes +
                'Sales Rep:\t%s' % main.notesRep
            )
        if docType == 'Event Sheet':
            file_handler.write(
                'Event Sheet\n\n'
                'Event Details:\n'
                '\tName:\t\t\t%s\n' % main.eventName +
                '\tDate:\t\t\t%s\n' % main.eventDate +
                '\tLocation/Address:\t%s\n' % main.eventLocation +
                '\tScheduled Times:\t%s-%s\n\n' % (main.startTime, main.endTime) +
                'Sales Rep:\t\t%s\n' % main.notesRep +
                'Event Lead:\t\t\n'
                'Other Staff:\t\t\n'
                'Setup Time:\t\t%s\n' % main.eventSetup +
                'Takedown Time:\t%s\n' % main.eventTakedown +
                'Point of Contact:\t%s\t%s\n' % (main.clientName, main.clientPhone) + 
                'Vehicle:\t\t\n'
                '\tAnticipated Miles:   \n'
                'Dress Code:\t\t%s\n' % main.eventDress +
                'Invoice Number:\t%s\n\n' % main.notesInv +
                'Staff Notes:\n\t%s' % main.notesNotes
            )
        if docType == 'Pack List':
            file_handler.write(
                'Pack List\n\n%s' % main.packageChoice
            )
        if docType == 'Contract':
            file_handler.write(
                'Name:   %s\t' % main.clientName +
                'Mailing Address:   \n' +
                'Phone:   %s\t' % main.clientPhone +
                'E-Mail:   %s\n\n' % main.clientEmail +

                '%s has requested services for %s, from %s to %s. Location: %s\n' % (main.clientName, main.eventName, main.startTime, main.endTime, main.eventLocation) +
                'The agreed upon amount to be paid will be $________\n' +
                '* If overtime is desired by client the charge is due in advance of overtime ($35 per hour)\n\n' +

                '1.\tA deposit is required for preparations for the event and to secure services for the date listed above. The amount shall be paid in the amount of $________ when signing this agreement. If %s cancels at any time before the date of the event, they can transfer the fee to another event within one (1) year, providing the new date is acceptable and available to ANDX Ent. ANDX Ent. may also choose to refund %s zero, part, or full of their deposit.\n' % (main.clientName, main.clientName) +
                '2.\tThe remaining balance of $________ shall be paid by %s before said event ANDX Ent., at its sole option, can terminate this agreement and refuse to provide said services if payment of the remaining balance is not made in a timely manner (minimum of one week prior to event). Checks will be mailed to: 1582 N. Holmes Ave., Idaho Falls, ID, 83401\n' % main.clientName +
                '3.\tANDX Ent. is not liable for any complications outside their control, including power interruptions, crowd control, or any other similar reason.\n' +
                '4.\t%s is also responsible for damage to property of ANDX Ent. at event. Charges from damaged equipment will be made by ANDX Ent. and be known to %s by the end of the event.\n' % (main.clientName, main.clientName) +
                '5.\tIf there is any breach of this agreement by ANDX Ent., the maximum amount of damages that can be awarded to %s, including attorney fees and costs, shall be the total amount paid to ANDX Ent.\n' % main.clientName +
                '6.\t%s will be charged $40.00 for any returned checks.\n' % main.clientName +
                '7.\tANDX Ent. will provide the following Event Package:\n\n%s\n\n' % main.packageName +
                '8.\tOther requirements from our client:\n\n\n' +

                'Signature of the Client (%s): ____________________________________' % main.clientName
            )

# 
# NAME:     queueFiles
# PURPOSE:  Adds files to an array queue to be uploaded
# 
def queueFile(DRIVE, docType):
    temp_list = []
    global fileName
    fileName = '%s %s.txt' % (main.eventName, docType)
    createFile(fileName, docType)
    temp_list.append(fileName)
    temp_list.append(mimeType)
    file_metadata = tuple(temp_list)
    global file_queue
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