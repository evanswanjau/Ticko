#Ticket Booking Service using python command line
#Author: Evans Wanjau
#################################################

import sqlite3
conn = sqlite3.connect('Ticko.db')
c = conn.cursor()

# Insert a row of data
# c.execute("INSERT INTO event_details VALUES('Jameson Live', '20th December 2016', '22nd December 2016', 'Ngong Racecourse')")

# Save or commit the changes
# conn.commit()

# Close the connection
# conn.close()

# Collect data from the user
def collectUserData():
    print('######################################\n\nWelcome to Ticko')
    username = input('\nPlease enter your name: ')
    useremail = input('\nPlease enter your email: ')
    request = input('\nWhat would you like to do today ' + username + '\n ################################\n 1. Create an event\n 2.Delete an event \n 3. Edit Event \n 4.List all the events\n :')

    # Using if statements to get the required data
    if request == 1:
        collectEventData()
    elif request == 2:
        deleteEventData()
    elif request == 3:
        editEventData()
    elif request == 4:
        listEventData()

def collectEventData():
    eventname = input('Please enter event name: ')
    startdate = input('\nPlease enter event start date: (DD/MM/YYYY): ')
    enddate = input('\nPlease enter event end date: (DD/MM/YYYY): ')
    venue = input('\nPlease enter event venue: ')

    # Create table
    #c.execute('''CREATE TABLE event_details(name, startdate, enddate, venue, username, email)''')
    # Add data to db
    c.execute("INSERT INTO event_details VALUES('eventname', 'startdate', 'enddate', 'venue', 'username', 'useremail')")
    if c.execute == True:
        print('Event created successfully :)')
    else:
        print('Event not created')


collectEventData()
