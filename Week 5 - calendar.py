def leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
     
 
def day_of_week_jan1(year):
    a = year - 1
    d = (6*(a%400) + 4*(a%100) + 5*(a%4) +  1) % 7
    return d

def num_days_in_month(month_num, leap_year):
    if month_num in [1,3,5,7,8,10,12]:
        return 31
    elif month_num == 2:
        if leap_year:
            return 29
        else: return 28
    else:
        return 30

def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    month_names = {1: 'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    ret_val = [month_names[month_num]]
    week = '   ' * first_day_of_month
    date = 1
    day = first_day_of_month
    while date <= num_days_in_month:
        while day <= 6:
            week += '%3s'%str(date)
            day += 1
            date += 1
            if date > num_days_in_month:
                break
        day = 0
        ret_val.append(week)
        week = ''
    return ret_val

'''def print_cal_month(list_of_str):
    ret_val = ''
    for l in list_of_strL:
        ret_val += l.replace('','*')
        ret_val += '\n'
    return ret_val'''
 
def construct_cal_year(year):
    ret_val = [str(year)]
    isleap = leap_year(year)
    for month in range(1,13):
        if month == 1:
            first = day_of_week_jan1(year)
            days = 31
        else:
            first = (first+days) % 7
            days = num_days_in_month(month, isleap)
        month_list = construct_cal_month(month, first, days)
        ret_val.append(month_list)
    return ret_val

def display_calendar(year):
    calendar = ""
    calendar_year = construct_cal_year(year)
    calendar_year.pop(0)
    for i , month in enumerate(calendar_year):
        for j, week in enumerate(month):
            calendar += week
            calendar += '\n'
            if j == 0:
                calendar += '  S  M  T  W  T  F  S\n'
        if i != 11:
            calendar += '\n'
    return calendar

l = display_calendar(2018)
print(l)
