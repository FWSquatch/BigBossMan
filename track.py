#!/usr/bin/env python3

import time, requests

# Get the latest data from Google Sheets
def get_data():
    r = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTcG1Ttk2lWintf5_ahUXs232B8CHC9eJNFDyvL_37o_PLivPO7J2KnYoMBkl0W66csZBGcunJgPs2w/pub?gid=1203981429&single=true&output=csv')
    data = r.text.split("\r\n") # Grab csv file and split it into rows
    mylist = []
    
    for element in data:
        mylist.append(element.split(',')) # Create 2D list
    return mylist

# Find current time and return the next due date
def get_due_date():
    currentTime = time.time()
    if currentTime <= 1586736000:
        dueDateCell = 4
    elif currentTime <= 1587340800:
        dueDateCell = 6
    elif currentTime <= 1587945600:
        dueDateCell = 8
    elif currentTime <= 1588550400:
        dueDateCell = 10
    else:
        dueDateCell = 12 
    return dueDateCell

# Check for student's assignments
def check_student(name = "You must supply a name!"):
    response = ""
    if name != "null":
        data = get_data()  
        dueDate = data[0][get_due_date()]
        response = "The next due date is: " + dueDate
        for row in data:
            if name.capitalize() in row: # If first or last name in the row, then respond
                response += "\n" + row[1] + " " + row[0] + " must complete " + row[2] + " " + row[4]
    else:
        response = 'You must supply a name!'
    return response