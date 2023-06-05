def add_time(start_time, duration, start_day=None):
    # Extract the components of the start time
    start_components = start_time.split()
    start_hour, start_minute = map(int, start_components[0].split(':'))
    start_period = start_components[1].upper()

    # Extract the components of the duration time
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Convert start time to 24-hour format
    if start_period == 'PM' and start_hour != 12:
        start_hour += 12

    # Calculate the total minutes
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

    # Calculate the new time and days later
    new_hour = total_minutes // 60 % 24
    new_minute = total_minutes % 60
    days_later = total_minutes // 1440

    # Determine the period (AM/PM) of the new time
    if new_hour >= 12:
        period = 'PM'
    else:
        period = 'AM'

    # Convert the new hour to 12-hour format
    if new_hour > 12:
        new_hour -= 12
    elif new_hour == 0:
        new_hour = 12

    # Determine the day of the week if start_day is provided
    if start_day:
        start_day = start_day.lower().capitalize()
        days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        start_day_index = days_of_week.index(start_day)
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        day_of_week = f', {new_day}'
    else:
        day_of_week = ''

    # Generate the final result string
    result = f'{new_hour}:{new_minute:02d} {period}'

    if days_later == 1:
        result += ' (next day)'
    elif days_later > 1:
        result += f' ({days_later} days later)'

    result += day_of_week

    print(result)

add_time("11:30 AM", "2:32", "Monday")
add_time("11:43 PM", "24:20", "tueSday")
add_time("3:00 PM", "3:10")
