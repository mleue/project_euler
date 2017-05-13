import itertools

class DateIterator:
  def __init__(self, day, month, year):
    """initialize day, month, year, the month_days lookup and set if it is a leap year"""
    #so that the initial output will be the initial input date
    self.day = day-1
    self.month = month
    self.year = year
    self.month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
                       7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    self.set_if_leap_year()

  def set_if_leap_year(self):
    """alter the value of number of days in February in the month_days lookup if we have a leap year"""
    if self.year % 4 == 0 and not self.year % 400 == 0:
      self.month_days[2] = 29
    else:
      self.month_days[2] = 28

  def __iter__(self):
    """return reference to itself"""
    return self

  def advance_year(self):
    """advance by one year"""
    self.year += 1
    self.month = 1
    self.day = 1
    self.set_if_leap_year()

  def advance_month(self):
    """advance by one month"""
    self.month += 1
    self.day = 1
    #check if we are in a new year
    if self.month > 12:
      self.advance_year()

  def __next__(self):
    """advance one day"""
    self.day += 1
    #check if we are in a new month
    if self.month_days[self.month] < self.day:
      self.advance_month()

    return self.day, self.month, self.year

if __name__ == '__main__':
  date_it = DateIterator(1, 1, 1901)
  weekdays = ['Tu', 'We', 'Th', 'Fr', 'Sa', 'Su', 'Tu']
  weekday_it = itertools.cycle(weekdays)
  count_sunday_first_day_of_month = 0
  for date, weekday in zip(date_it, weekday_it):
    if date[2] > 2000:
      break
    if date[0] == 1 and weekday == 'Su':
      count_sunday_first_day_of_month += 1
      #print(date, weekday)

  print("There are {} sundays as the first day of a month between 1,1,1901 and 31,12,2001"
        .format(count_sunday_first_day_of_month))
