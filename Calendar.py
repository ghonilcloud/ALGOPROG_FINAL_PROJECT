import calendar
import datetime

class Event:
    def __init__(self, day, month, year, description, colour):
        self.day = day
        self.month = month
        self.year = year
        self.description = description
        self.colour = colour
        # Basic format for an event, only consisting of days, months, years, and a description.

class CalendarApp:
    def __init__(self, year):
        # Gets the current date of the computer, which will later be highlighted yellow.
        today = datetime.date.today()

        self.year = year
        self.calendar = calendar.TextCalendar()
        self.events = [
            Event(today.day, today.month, today.year, description="Today", colour="yellow"),
            Event(day=2, month=1, year=2024, description="2023 Test January Red", colour="red"),
            Event(day=3, month=1, year=2024, description="2023 Test January Purple", colour="purple"),
            Event(day=4, month=1, year=2024, description="2023 Test January Blue", colour="blue"),
            Event(day=5, month=1, year=2024, description="2023 Test January Cyan", colour="cyan"),
            Event(day=7, month=1, year=2024, description="2023 Test January Yellow", colour="yellow"),
        ]

        self.global_holidays = [
            # Add Global holidays as needed
            Event(day=1, month=1, year=self.year, description="New Year's Day", colour="green"),
            Event(day=14, month=2, year=self.year, description="Valentine's Day", colour="green"),
            Event(day=17, month=3, year=self.year, description="St. Patrick's Day", colour="green"),
            Event(day=1, month=4, year=self.year, description="April Fools' Day", colour="green"),
            Event(day=1, month=5, year=self.year, description="May Day", colour="green"),
            Event(day=5, month=5, year=self.year, description="Cinco de Mayo", colour="green"),
            Event(day=1, month=6, year=self.year, description="International Children's Day", colour="green"),
            Event(day=4, month=7, year=self.year, description="Independence Day", colour="green"),
            Event(day=15, month=8, year=self.year, description="Assumption of Mary", colour="green"),
            Event(day=12, month=10, year=self.year, description="Columbus Day", colour="green"),
            Event(day=31, month=10, year=self.year, description="Halloween", colour="green"),
            Event(day=25, month=12, year=self.year, description="Christmas Day", colour="green"),
            Event(day=31, month=12, year=self.year, description="New Year's Eve", colour="green"),
            Event(day=25, month=1, year=self.year, description="Chinese New Year", colour="green"),
            Event(day=17, month=8, year=self.year, description="Indonesian Independence Day", colour="green"),
            Event(day=1, month=6, year=self.year, description="Pancasila Day", colour="green"),
            Event(day=12, month=8, year=self.year, description="Islamic New Year", colour="green"),
            Event(day=20, month=11, year=self.year, description="The Prophet Muhammad's Birthday", colour="green"),
            Event(day=1, month=5, year=self.year, description="Labor Day", colour="green"),
            # Holidays don't need a "colour" to be highlighted since if they are already on this list they are automatically highlighted.
        # Its just a placeholder, just to have something there. :/
        ]

    def option1_view(self):
        # Asks for the specific month for the user, code ensures the input by the user is between 1-12 and an integer.
        while True:
            try:
                month = int(input("Enter the month (1-12): "))
                if 1 <= month <= 12:
                    break
                else:
                    print("Invalid month. Please enter a number between 1 and 12.")

            except ValueError:
                print("Invalid input. Please enter a valid integer for the month.")

        # Asks the user to input a year, it only ensures that the year is a valid integer.
        while True:
            try:
                year = int(input("Enter the year: "))
                print(" ")
                print("-" * 40)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for the day.")

        # Creates the calendar for the selected month and year, using the imported calendar.
        selected_month_data = self.calendar.formatmonth(year, month)
        # events_list_data is used later on to take all the events within the month into a list, which will then be sorted based on the day for it to be displayed to the user.
        events_list_data = [event for event in self.events if event.month == month and event.year == year]
        # Creates a list called holidays_list_data, it then goes through each event in global_holidays and 
        holidays_list_data = [event for event in self.global_holidays if event.month == month]
        # All the data above is then sent to the "def highlight_days" in order to create the higlighted calendar that can then be outputted for the user.
        highlighted_calendar = self.highlight_days(selected_month_data, events_list_data, holidays_list_data)

        # Since the variable "month" is still just a number that the user inputted, this line of code is used to convert that number into the actual month name.
        # In this case, a "1" would mean "January", all the way up to "12" which would mean "December".
        month_name = calendar.month_name[month]
        # Prints out the title 
        print(f"\n{month_name} {year}\n")
        # Prints out the actual calendar with the higlighted days.
        print(highlighted_calendar)

        # All the holidays and events are then combined into the variable "total_events_data".
        total_events_data = events_list_data + holidays_list_data
        # They are all sorted from the least to highest in terms of the day date, months and years dont matter since only events within the same month and year is chosen.
        total_events_data.sort(key=lambda x: (x.day, x.month, x.year))

        # All the sorted events in "total_events_data" is then printed out in a for loop, only ending when all the events have been printed.
        print(f"\nAll Events in {month_name} {year}:")
        for event in total_events_data:
            print(f"{event.year}-{event.month:02d}-{event.day:02d}: {event.description}")
        print(" ")
        print("-" * 40)

    def option2_add(self, event=None):
        if event is None: #To make sure that the def doesn't start when running the program.
            while True: #Asks for the specific month for the user, code ensures the input by the user is between 1-12 and an integer.
                try:
                    month = int(input("Enter the month (1-12): "))
                    if 1 <= month <= 12:
                        break
                    else:
                        print("Invalid month. Please enter a number between 1 and 12.")

                except ValueError:
                    print("Invalid input. Please enter a valid integer for the month.")

            # Since each month has a different set of days, when displaying the prompt we need this so the user knows how many days within the month.
            # Later in the prompt it will display "Enter the day (1-[max days])", instead of sticking to 31 days for every month.
            max = calendar.monthrange(self.year, month)[1]

            # Ask the users which day do they want the event to be placed in, ensuring that the input is between 1 and the maximum amount of days in the month and an integer.
            while True:
                try:
                    day = int(input(f"Enter the day (1-{max}): "))
                    if 1 <= day <= max:
                        break
                    else:
                        print(f"Invalid day. Please enter a number between 1 and {max}.")

                except ValueError:
                    print("Invalid input. Please enter a valid integer for the day.")

            # Same thing, but this time it only asks for a year in the form of an integer.
            while True:
                try:
                    year = int(input("Enter the year: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer for the year.")

            # Asks for a description, there is no limit on integer or word count.
            description = input("Enter the event description: ")

            # A list of colours that will pop up in a list when the user is prompted to choose.
            valid_colours = ['red', 'blue', 'purple', 'cyan']

            # Ask the user to pick a colour, which will be placed in a list.
            while True:
                print("Choose a color for the event:")
                for i, colour in enumerate(valid_colours, start=1):
                # Iterates through the entire list while also keeping count, starting from 1.
                    print(f"{i}. {colour}")

                # Once the list is printed, it will prompt the user to pick an option from 1 to the max amount of colours on the list. Colours can be added or removed as needed.
                # But as of this moment all the colours for ANSI has been added.
                try:
                    colour_choice = int(input("Enter the number corresponding to your color choice: "))
                    if 1 <= colour_choice <= len(valid_colours):
                        break
                    else:
                        print(f"Invalid choice. Please enter a number between 1 and {len(valid_colours)}.")

                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            # Since we added +1 to make sure the list started from 1 and not 0, It has to be reversed again. And on top of that it is still in the form of an int, and not an str.
            colour = valid_colours[colour_choice - 1]

            # All info is then placed into the event class.
            event = Event(day, month, year, description, colour)

            # Asks the user if they would like the event to be repeated for the following weeks, users can only put yes or no.
            while True:
                repeat_event_input = input("Do you want to repeat this event in the following weeks? (Yes/No): ").lower()
                if repeat_event_input in ['yes', 'no']:
                    repeat_event_input == 'yes'
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            # If the user does want the event to be repeated, it will then ask the user for how much.
            if repeat_event_input == 'yes':
                while True:
                    try:
                        repeat_weeks = int(input("Enter the number of weeks to repeat the event: "))
                        if repeat_weeks >= 1:
                            break
                        else:
                            print("Invalid input. Please enter a number greater than or equal to 1.")
                    except ValueError:
                        print("Invalid input. Please enter a valid integer for the number of weeks.")
            else:
                repeat_weeks = 0

            # If the user inputs 2, then the following 2 weeks will have an event added that matches the exact same description, however it will only be in the next following week.
            if repeat_weeks > 0:
                for i in range(1, repeat_weeks + 1):
                    next_week_date = datetime.date(year, month, day) + datetime.timedelta(weeks=i)
                    # If the user inputs 2, then the following 2 weeks will have an event added that matches the exact same description, however it will only be in the next following week.
                    # This is done by adding the user's choice for the date, but adding an extra week (7 days) onto it.

                    # The date of this extra week is then noted and placed into the "next_event" variable, which will then be appended onto the "events" list in __init__
                    # Description will match the previous events, but it will have a "(Repeated)" mark at the end.
                    next_event = Event(day=next_week_date.day, month=next_week_date.month, year=next_week_date.year, description=f"{description} (Repeated)", colour=colour)
                    self.events.append(next_event)

            # The event is then added onto the 'events' list within __init__, along with any repeated events (with a distance of 7 days)
            self.events.append(event)
            print(" ")
            print("Event has been sucessfully added.")
            print(" ")
            print("-" * 40)

    def option3_remove(self):
        # This asks for the user to choose a year, it makes sure the users picks an integer.
        while True:
            try:
                year = int(input("Enter the year: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for the year.")

        # This checks if the chosen month is between 1-12, it makes sure the users picks an integer.
        while True:
            try:
                month = int(input("Enter the month (1-12): "))
                if 1 <= month <= 12:
                    print(" ")
                    print("-" * 40)
                    break
                else:
                    print("Invalid month. Please enter a number between 1 and 12.")

            except ValueError:
                print("Invalid input. Please enter a valid integer for the month.")

        # "event for event in self.events" goes over(iterates) every event in the "self.events" list in "__init__"
        # "if event.year == year and event.month == month" this checks for any event within the user's chosen month and year are the only ones selected for the "events_in_month" list.
        # This is to prevent other events from being placed in the list. ^
        events_in_month = [event for event in self.events if event.year == year and event.month == month]

        # When the selected month has no events located within it, this output will be chosen.
        if not events_in_month:
            print(f"No events found in {calendar.month_name[month]} {year}.")
            return

        # But if there is an event, it will output the events in a list.
        # Format:
        # [Number in list]. [Day]-[Month]-[Year]: [Description]
        print(f"\nEvents in {calendar.month_name[month]} {year}:")
        for i, event in enumerate(events_in_month):
            print(f"{i + 1}. {event.day}-{event.month}-{event.year}: {event.description}")

        # Asks the user to pick an event from the list provided, user must pick an integer within the list.
        while True:
            try:
                print(" ")
                print("-" * 40)
                print(" ")
                index = int(input(f"Enter the number of the event to remove (1-{len(events_in_month)}): "))
                if 1 <= index <= len(events_in_month):
                    break
                else:
                    print(f"Invalid index. Please enter a number between 1 and {len(events_in_month)}.")

            except ValueError:
                print("Invalid input. Please enter a valid integer for the index.")

        # The integer inputted is then used to select the event within the "events_in_month" list. Since lists start from 0, the "-1" is needed.
        # Event is then removed from the events_in_month list.
        removed_event = events_in_month[index - 1]
        self.events.remove(removed_event)
        print(f"Event on {removed_event.day}-{removed_event.month}-{removed_event.year} removed successfully.")
        print(" ")
        print("-" * 40)

    def option4_summary(self, year=None):
        # Asks user for the year, ensures that it is a positive integer.
        if year is None:
            while True:
                try:
                    year = int(input("Enter the year to summarize: "))
                    if year >= 1:
                        break
                    else:
                        print("Invalid year. Please enter a valid positive integer.")

                except ValueError:
                    print("Invalid input. Please enter a valid integer for the year.")

        # Uses the user-inputed year for the title.
        print(f"\nSummary for {year}:\n")
        print("-" * 40)

        # Iterates through EVERY month within the year.
        for month in range(1, 13):
            # Creates the calendar for the selected month and year, using the imported calendar.
            selected_month_data = self.calendar.formatmonth(year, month)
            # events_list_data is used later on to take all the events within the month into a list, which will then be sorted based on the day for it to be displayed to the user.
            events_list_data = [event for event in self.events if event.month == month and event.year == year]
            # Creates a list called holidays_list_data, it then goes through each event in global_holidays and 
            holidays_list_data = [event for event in self.global_holidays if event.month == month]
            # All the data above is then sent to the "def highlight_days" in order to create the higlighted calendar that can then be outputted for the user.
            highlighted_calendar = self.highlight_days(selected_month_data, events_list_data, holidays_list_data)

            # Since the variable "month" is still just a number that the user inputted, this line of code is used to convert that number into the actual month name.
            # In this case, a "1" would mean "January", all the way up to "12" which would mean "December".
            month_name = calendar.month_name[month]
            # Prints out the title 
            print(f"\n{month_name} {year}\n")
            # Prints out the actual calendar with the higlighted days.
            print(highlighted_calendar)

            # All the holidays and events are then combined into the variable "total_events_data".
            total_events_data = events_list_data + holidays_list_data
            # They are all sorted from the least to highest in terms of the day date, months and years dont matter since only events within the same month and year is chosen.
            total_events_data.sort(key=lambda x: (x.day, x.month, x.year))

            # Uses the user-inputed year for the title of the event list of each month.
            print(f"\nAll Events in {month_name} {year}:")
            for event in total_events_data:
                print(f"{event.year}-{event.month:02d}-{event.day:02d}: {event.description}")

            print(" ")  # Just adding a space to make it look pretty :3
            print("-" * 40)  # Add a line between each month.

    def highlight_days(self, selected_month_data, events_list_data, holidays_list_data):
        # Split the calendar's days each into their own lines, leaving out the title and empty line that also gets printed out.
        lines = selected_month_data.split('\n')[2:-1]
        # Any days(lines) that get highlighted will be placed here to be selected.
        highlighted_lines = []  

        # Iterate through each individual line which contains a day number.
        for line in lines:
            highlighted_line = ''  # Initialize an empty string to store the highlighted characters.

            # Split the calendar into its own individual days.
            day = line.split()
            for day in day:
                day = day.strip()  # Remove leading/trailing spaces from each day.

                # Check if the day is in the list of days with events. If so, it highlights it in the chosen colour of the user.
                if int(day) in [events.day for events in events_list_data]:
                    matching_events = [event for event in events_list_data if event.day == int(day)]
                    if matching_events:
                        # Use the colour of the first matching event
                        colour = matching_events[0].colour
                        if colour == "yellow":
                            highlighted_line += f"\033[1;33m{day}\033[0m"  # Highlight in yellow
                        elif colour == "red":
                            highlighted_line += f"\033[1;31m{day}\033[0m"  # Highlight in red, uses ANSI escape codes.
                        elif colour == "blue":
                            highlighted_line += f"\033[1;34m{day}\033[0m"  # Highlight in blue
                        elif colour == "purple":
                            highlighted_line += f"\033[1;35m{day}\033[0m"  # Highlight in purple
                        elif colour == "cyan":
                            highlighted_line += f"\033[1;36m{day}\033[0m"  # Highlight in cyan
                # Check if the day is in the list of global holidays. If so, it higlights it green.
                elif int(day) in [holiday.day for holiday in holidays_list_data]:
                    highlighted_line += f"\033[1;32m{day}\033[0m" # The "32" determines the colour green.
                # If it is not an event or holiday, it will not be highlighted.
                else:
                    highlighted_line += day  
                highlighted_line += ' '  # Add a space after each day.
            
            # Add all the days that were higlighted green or red onto the "highlighted_lines" list.
            highlighted_lines.append(highlighted_line.strip())

        # Join the highlighted lines with newline characters and return the resulting highlighted calendar to either "option1_view" or "option4_summary", depending on which called it.
        return '\n'.join(highlighted_lines)

if __name__ == "__main__":
    year = 2023 #Default year used
    calendar_app = CalendarApp(year)

    while True:
        print("\nOptions:")
        print("1. View Calendar")
        print("2. Add Events")
        print("3. Remove Events")
        print("4. Summary")
        print("5. Exit")
        print(" ") # Just adding a space to make it look pretty :3
        print("-" * 40) # Add a line between each month

        print(" ")
        user_choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

        if user_choice == "1":
            # Display events for the chosen month and year with highlighted days
            calendar_app.option1_view()

        elif user_choice == "2":
            # Add event via terminal input
            calendar_app.option2_add()

        elif user_choice == "3":
            # Remove events via terminal input
            calendar_app.option3_remove()

        elif user_choice == "4":
            # Display year summary
            calendar_app.option4_summary()

        elif user_choice == "5":
            # Bye bye Mr.Jude (0_0)
            print("Exiting the program. Goodbye!")
            break