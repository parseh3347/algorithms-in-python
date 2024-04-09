# import datetime
from datetime import datetime,timedelta
import winsound, time

# create two dates with year, month, day, hour, minute, and second
def diff_time():
    # date1 = datetime(2017, 6, 27, 18, 25, 30)
    date1 = datetime.now()
    date2 = datetime(2023, 6, 21, 8, 21, 10)

    diff_date = date1-date2
    print("Difference: ", diff_date)


diff_time()

        





# diff_time =diff_date+timedelta(days=5, hours=4)
# print("Difference: ", diff_time)