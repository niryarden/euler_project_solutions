# answer: 171

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

the_count = 0 # the final count of the sundays in the begining of the month
year = 1900
weekday_count = 2 # 1 Jan 1900 was a Monday
leap = False

while year < 2001:
    #skiping 1900
    if year == 1900:
        weekday_count += sum(months)
        year += 1
        continue

    #was last year a leap year?
    if leap == True:
        leap = False
        months[1] = 28

    #is this year is a leap year?
    if year % 4 == 0:
        if year % 100 != 0:
            leap = True
            months[1]= 29
        elif year % 400 == 0:
            leap = True
            months[1] = 29
    # looping through all the months
    for month in months:
        if weekday_count % 7 == 1:
            the_count += 1
        weekday_count += month
    year += 1

print(f"answer {the_count}")
