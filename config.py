import os.path

# GLOBALS
scopes = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/drive']

# DATE & TIME VARIABLES
eventSum = 'Dinner with friends'        #placeholder
startDate = '2019-11-15'                #placeholder
endDate = '2019-11-15'                  #placeholder
startTime = '19:00'                     #placeholder
endTime = '22:00'                       #placeholder
    # TODO LIST:
    #   - full string format: 'YYYY-MM-DD' + 'T' + 'HH:MM:SS'
    #   - 'start' and 'end' variables are to be user-input from Django form
    #   - 'Time' forms will autocorrect from single digit (eg. '9') to full length (eg. 09:00)
    #   - 'Date' forms will be input as format requires until string parsing and reordering can be bothered
    #   - for Google Calendar
    #       - always add on another ':00' for 'seconds'
    #       - add '12:00' if PM
    #   - for Google Drive
    #       - create new folder for events
    #       - parse 'startDate' for month, and create new month folder as necessary
    #       - create new files in Drive without having to keep them on local storage
gmtOffset = '-7:00' # for GMT-7 or MDT
