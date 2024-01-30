import datetime

# In-memory data structure to store events
events = {}

def add_event():
    title = input("Enter event title: ")
    description = input("Enter event description: ")

    # Validate date and time format
    while True:
        date_str = input("Enter event date (YYYY-MM-DD): ")
        time_str = input("Enter event time (HH:MM): ")

        try:
            event_date = datetime.datetime.strptime(date_str + " " + time_str, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("Invalid date or time format. Please try again.")

    events[title] = {
        'title': title,
        'description': description,
        'date': event_date.strftime("%Y-%m-%d"),
        'time': event_date.strftime("%H:%M")
    }

    print("Event added successfully!\n")

def list_events():
    if not events:
        print("No events found.")
        return

    sorted_events = sorted(events.values(), key=lambda x: (x['date'], x['time']))
    for event in sorted_events:
        print(f"\nTitle: {event['title']}\nDescription: {event['description']}\nDate: {event['date']}\nTime: {event['time']}\n")

def delete_event():
    title_to_delete = input("Enter the title of the event to delete: ")

    # Make the search case-insensitive
    matching_titles = [title for title in events if title.lower() == title_to_delete.lower()]

    if matching_titles:
        for title in matching_titles:
            del events[title]
        print("Event(s) deleted successfully!\n")
    else:
        print("Event not found.\n")

def edit_event():
    title_to_edit = input("Enter the title of the event to edit: ")
    if title_to_edit in events:
        print("Enter new details for the event (leave blank to keep existing):")
        new_title = input(f"Current Title: {events[title_to_edit]['title']}\nNew Title: ") or events[title_to_edit]['title']
        new_description = input(f"Current Description: {events[title_to_edit]['description']}\nNew Description: ") or events[title_to_edit]['description']
        new_date = input(f"Current Date: {events[title_to_edit]['date']}\nNew Date (YYYY-MM-DD): ") or events[title_to_edit]['date']
        new_time = input(f"Current Time: {events[title_to_edit]['time']}\nNew Time (HH:MM): ") or events[title_to_edit]['time']

        # Validate new date and time format
        try:
            datetime.datetime.strptime(new_date, '%Y-%m-%d')
            datetime.datetime.strptime(new_time, '%H:%M')
        except ValueError:
            print("Invalid date or time format. Event not edited.")
            return

        # Update event details
        events[title_to_edit] = {'title': new_title, 'description': new_description, 'date': new_date, 'time': new_time}
        print(f"Event '{title_to_edit}' edited successfully.")
    else:
        print("Event not found.")
def search_events():
    search_term = input("Enter a date or keyword to search for events: ")
    matching_events = [event for event in events.values() if search_term.lower() in (event['date'].lower() + event['title'].lower() + event['description'].lower())]

    if matching_events:
        for event in matching_events:
            print(f"\nTitle: {event['title']}\nDescription: {event['description']}\nDate: {event['date']}\nTime: {event['time']}\n")
    else:
        print("No matching events found.\n")

# user interface
while True:
    print("\nEvent Scheduler Menu:")
    print("1. Add Event")
    print("2. List Events")
    print("3. Delete Event")
    print("4. Edit Events")
    print("5. Search Events ")
    print("6. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_event()
    elif choice == '2':
        list_events()
    elif choice == '3':
        delete_event()
    elif choice == '4':
        edit_event()
    elif choice == '5':
        search_events()
    elif choice == '6':
        print("Exiting Event Scheduler. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.\n")

        

