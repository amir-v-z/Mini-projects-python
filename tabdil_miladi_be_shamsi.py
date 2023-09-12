# pip install pytz
from persiantools.jdatetime import JalaliDate
from datetime import datetime
date = datetime.strptime(input("Enter time example(2003-07-24): "), '%Y-%m-%d')

persian_date = JalaliDate.to_jalali(date)
day_name = persian_date.strftime("%c").split(" ")[0]
print(f"{day_name}: {persian_date}")