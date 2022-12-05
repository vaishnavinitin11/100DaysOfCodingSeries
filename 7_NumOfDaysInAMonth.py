# Day 7 coding Statement:  Write a program to find Number of days in a given month of a given year

month=int(input('Enter month: '))
year=int(input('Enter year: '))

def daysinamonth(month,year):
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        print('31')
    elif month == 2:
        if year%4==0:
            print('29')
        else:
            print('28')
    else:
        print('30')

daysinamonth(month,year)