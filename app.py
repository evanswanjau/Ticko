#Ticket Booking Service using python command line
#Author: Evans Wanjau
#################################################

import sqlite3
conn = sqlite3.connect('Ticko.db')
c = conn.cursor()

# Collect personal data from the user
def collectUserData():
    print(' ########################\n Welcome to Ticko')
    global username
    global useremail
    username = input('\n Please enter your name: ')
    useremail = input('\n Please enter your email: ')

    # Data verification
    ERRORS = [' \n']
    if username == '':
        ERRORS.append(' # Username cannot be empty')
    if useremail == '':
        ERRORS.append(' # Email cannot be empty')
    if '@' not in useremail:
      ERRORS.append(' # Missing @ in email')
    if '.' not in useremail:
      ERRORS.append(' # Missing . in email')
    if ERRORS != [' \n']:
        for error in ERRORS:
            print(error)
        collectUserData()
    if ERRORS == [' \n']:
        print(' Data entered successfully')
        collectRequestData()

# Ask user for request function
def collectRequestData():
    request = input('\n           TICKO MENU \n ################################\n # 1. Create an event\n # 2. View events \n # 3. Edit Event \n # 4. Delete an event\n # 5. Exit app\n\n')

    # Using if statements to get the required data
    if request == '1':
        collectEventData()
    elif request == '2':
        listEventData()
    elif request == '3':
        updateEventData()
    elif request == '4':
        deleteEventData()
    elif request == '5':
        exitApp()
    else:
        print('* You have entered an incorrect value')
        collectRequestData()


# collectEventData function
def collectEventData():
    eventname = input('Please enter event name: ')
    startdate = input('\nPlease enter event start date: (DD/MM/YYYY): ')
    enddate = input('\nPlease enter event end date: (DD/MM/YYYY): ')
    venue = input('\nPlease enter event venue: ')

    def confirmEventData():
        print('\n ############################ \n' + ' # Event: ' + eventname + '\n # Beginning: ' + startdate + '\n # Till: ' + enddate + '\n # Created by: ' + username + '\n # Contact: ' + useremail)
        event = input('\n Reply with (y/n) or (yes/no) \n Is this the event you want to create?')
        if event == 'y' or event == 'yes':
            c.execute("INSERT INTO event_details VALUES (?,?,?,?,?,?)", (eventname, startdate, enddate, venue, username, useremail))
            # Save or commit the changes
            conn.commit()
            # Close the connection
            conn.close()
            # Message
            print(' Event created successfuly')
            collectRequestData()
        elif event == 'n' or event == 'no':
            collectRequestData()
        else:
            print('You need to reply with the specified details (y/n) or (yes/no)')
            confirmEventData()
    confirmEventData()


# listEventData function
def listEventData():
    for row in c.execute('SELECT ROWID, name, venue FROM event_details'):
        print(row)
    def confirmBookTicket():
        book = input('\n Reply with (y/n) or (yes/no) \n Do you want to book a ticket? ')
        if book == 'y' or book == 'yes':
            BookTicket()
        elif book == 'n' or book == 'no':
            collectRequestData()
        else:
            print('You need to reply with the specified details (y/n) or (yes/no)')
            confirmBookTicket()
    confirmBookTicket()


#Book ticket function
def BookTicket():
    tStr = input(' Please enter event ID of event you want to choose: ')
    t = int(tStr)
    for row in c.execute('SELECT * FROM event_details WHERE ROWID =:t', {"t":t}):
        print(row)
    def confrimDataTicket():
        tip = input('\n Reply with (y/n) or (yes/no) \n Is this the event you want to choose?')
        if tip == 'y' or tip == 'yes':
            # Sql add data
            for event in c.execute('SELECT name FROM event_details WHERE ROWID =:t', {"t":t}):
                event = str(event)
            eventid = t
            c.execute("INSERT INTO Tickets VALUES (?, ?, ?, ?)", (username, useremail, eventid, event))
            # Save or commit the changes
            conn.commit()
            # Close the connection
            conn.close()
            # Message
            print(' Ticket generated successfuly')
            collectRequestData()
        elif tip == 'n' or tip == 'no':
            collectRequestData()
        else:
            print(' You need to reply with the specified details (y/n) or (yes/no)')
            confirmDataUpdate()
    confrimDataTicket()


#Update funtion
def updateEventData():
    IDStr = input('Enter ID of row you\'d like to update: ')
    ID = int(IDStr)
    eventname = input('\nPlease enter event name: ')
    startdate = input('\nPlease enter event start date: (DD/MM/YYYY): ')
    enddate = input('\nPlease enter event end date: (DD/MM/YYYY): ')
    venue = input('\nPlease enter event venue: ')

    # Confirm Update
    def confirmEventUpdate():
        print('\n ############################ \n' + ' # Event: ' + eventname + '\n # Beginning: ' + startdate + '\n # Till: ' + enddate + '\n # Change by: ' + username + '\n # Contact: ' + useremail)
        event = input('\n Reply with (y/n) or (yes/no) \n Is this the event you want to update?')

        if event == 'y' or event == 'yes':
            # Sql update
            sql = """
            UPDATE event_details
            SET name = ?, startdate = ?, enddate = ?, venue = ?, username = ?, email = ?
            WHERE ROWID = ?
            """
            c.execute(sql, (eventname, startdate, enddate, venue, username, useremail, ID))

            # Save or commit the changes
            conn.commit()

            # Close the connection
            conn.close()

            # Message
            print(' Event updated successfuly')
            collectRequestData()
        elif event == 'n' or event == 'no':
            collectRequestData()
        else:
            print('You need to reply with the specified details (y/n) or (yes/no)')
            confirmEventUpdate()
    confirmEventUpdate()


#Delete event function
def deleteEventData():
    IDStr = input(' Enter ID of row you\'d like to delete: ')
    ID = int(IDStr)

    # Confirm Delete
    def confirmEventDelete():
        for row in c.execute('SELECT * FROM event_details WHERE ROWID =:ID', {"ID":ID}):
            print(row)
        event = input('\n Reply with (y/n) or (yes/no) \n Is this the event you want to delete?')

        if event == 'y' or event == 'yes':
            # Sql delete
            c.execute('DELETE FROM event_details WHERE ROWID = :ID', {"ID":ID})
            # Save or commit the changes
            conn.commit()
            # Close the connection
            conn.close()
            # Message
            print(' Event deleted successfuly')
            collectRequestData()
        elif event == 'n' or event == 'no':
            collectRequestData()
        else:
            print('You need to reply with the specified details (y/n) or (yes/no)')
            confirmEventDelete()
    confirmEventDelete()


#Exit app function
def exitApp():
    end = input('\nReply with (y/n) or (yes/no) \nAre you sure you want to exit app? ')
    if end == 'y' or end == 'yes':
        exit()
    elif end == 'n' or end == 'no':
        collectRequestData()
    else:
        print('You need to reply with the specified details (y/n) or (yes/no)')
        exitApp()
collectUserData()
