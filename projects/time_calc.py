def add_time(start, duration, start_day=None):
    # Define days of the week
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    
    # Parse the start time
    start_parts = start.split()
    start_time = start_parts[0]
    period = start_parts[1]
    
    start_hour, start_minute = map(int, start_time.split(':'))
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0
    
    # Parse the duration time
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Calculate the new time
    end_minute = start_minute + duration_minute
    end_hour = start_hour + duration_hour + (end_minute // 60)
    end_minute %= 60
    days_later = end_hour // 24
    end_hour %= 24
    
    # Determine the new period and hour
    new_period = 'AM' if end_hour < 12 else 'PM'
    if end_hour == 0:
        end_hour = 12
    elif end_hour > 12:
        end_hour -= 12
    
    # Determine the new day of the week if provided
    if start_day:
        start_day = start_day.capitalize()
        start_day_index = days_of_week.index(start_day)
        end_day_index = (start_day_index + days_later) % 7
        end_day = days_of_week[end_day_index]
    else:
        end_day = None
    
    # Construct the new time string
    new_time = f"{end_hour}:{end_minute:02d} {new_period}"
    
    if end_day:
        new_time += f", {end_day}"
    
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
    
    return new_time

# Test cases
print(add_time('3:00 PM', '3:10'))
print(add_time('11:30 AM', '2:32', 'Monday'))
print(add_time('11:43 AM', '00:20'))
print(add_time('10:10 PM', '3:30'))
print(add_time('11:43 PM', '24:20', 'tueSday'))
print(add_time('6:30 PM', '205:12'))
