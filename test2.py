import datetime
import time

def timeBetweenNowAndThen(dateInput):
    today = datetime.datetime.now()
    todayYearMonthDay = today.strftime("%Y" + " %m" + " %d")
    todayUnix = time.mktime(today.timetuple()) * 1000
    userYear = dateInput[:4]
    userMonth = dateInput[5:7]
    userDay = dateInput[8:11]
    userYearMonthDay = datetime.date(
        int(userYear), int(userMonth), int(userDay))
    userUnixTime = (time.mktime(userYearMonthDay.timetuple()) * 1000)
    unixBetweenDates = todayUnix - userUnixTime
    unixYearsBetween = unixBetweenDates / 31_536_000_000
    unixMonthsBetween = (unixBetweenDates -
                         (int(unixYearsBetween) * 31_536_000_000)) / 2_629_800_000
    unixDaysBetween = ((unixBetweenDates - (int(unixYearsBetween) * 31_536_000_000)
                        ) - (int(unixMonthsBetween) * 2_629_800_000)) / 86_400_000

    result = str(int(unixYearsBetween)), " Year(s), ", str(int(
        unixMonthsBetween)), " Month(s) and ", str(int(unixDaysBetween)), " Day(s)"

    string = ""
    for items in result:
        string = string + items
    return string


print("\nEnter date in format YYYY-MM-DD:")
userYYYY_MM_DD = input()
print("\nTime since now and date entered:\n",
      timeBetweenNowAndThen(userYYYY_MM_DD), "\n")