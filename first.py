from datetime import datetime, date
import re

output_string  = input('Enter date in format YYYY-MM-DD: ') # '2003-12-12'
invalid_date_message = 'Invalid date: ' + output_string

match = re.search(r'(\d{4})-(\d{2})-(\d{2})', output_string)

if match is None:
    print(invalid_date_message)
    exit()

now = date.today()
input_year = int(match.group(1))
input_month = int(match.group(2))
input_day = int(match.group(3))

try:
    day = date(
        year=input_year,
        month=input_month, 
        day=input_day
        )
except ValueError:
    print(invalid_date_message)
    exit()

diff = now - day
diff_days = (str)(diff.days)

print('Difference between now and entered date: ' + diff_days + ' day(s)')