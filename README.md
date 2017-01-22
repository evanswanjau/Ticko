# Ticko
Ticket Booking Service | CMD

For this project, I will be creating a service for use at service stations where ticket bookings can be made. I should be able to create events, delete events, edit event and generate tickets (of various types).

As a user, I should be able to perform the following operations:

event create <event_details> - Creates a new event in the database table.
Event details should contain the following fields
Event name
Event start date
Event end date
Event venue

event delete <event_id> - Deletes an existing event from the database table.

event edit <event_id> <new_event_details> - Edit an already existing event from the database.

event list - Lists all the events in the database

event view <event_id> - View all the tickets that have been generated for that event.

ticket generate <e_mail> - Generates a new ticket and send it to the supplied e-mail address (if supplied. If not run ticket send <ticket_id> <e_mail> to send the ticket).

Once a ticket has been generated, send reminders at weekly intervals to remind the user about the event. (Extra Credit)

ticket invalidate <ticket_id> - Invalidates a ticket.
