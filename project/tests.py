# 
# This file is used for unit testing of individual functions
# 

import main

# Test auth() function
# Expected Result: SUCCESS
auth('calendar')
auth('drive')

# Test auth() function
# Expected Result: FAILURE
auth('1')