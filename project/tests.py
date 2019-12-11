# 
# This file is used for unit testing of individual functions
# 

from . import main

# Test auth() function
# Expected Result: SUCCESS
auth('calendar')
auth('drive')
auth('gmail')

# Test auth() function
# Expected Result: FAILURE
auth('1')

    # Check to see what it entered into the calendar
    print('''*** %r event added:
    Start: %s
    End:   %s''' % (e['summary'].encode('utf-8'),
        e['start']['dateTime'], e['end']['dateTime']))

    # Check to see what it uploaded into the drive
    if result:
            print('Uploaded "%s" (%s)' % (filename, result['mimeType']))