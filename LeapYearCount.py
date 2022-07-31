import datetime
from datetime import *

def list_of_leapyear(ele,leap_years):
    if ele % 2 != 0:
        n = ele - 1
    else:
        n = ele
    if n % 10 == 0:
        n = 10
    elif n % 8 == 0:
        n = 8
    elif n % 6 == 0:
        n = 6
    elif n % 4 == 0:
        n = 4
    elif n % 2 == 0:
        n = 2
    i = 0
    j = n
    while i < ele:
        print("\t{0}".format(leap_years[i:j]))
        i = j
        j += n

while True:
    print("\t\t***Leap Years from Date of Birth***")
    class leap_year_count():
        def __init__(self,b_day):
            self.b_day = b_day
        def year(self):
            try:
                today = date.today()
                birthdate=datetime.strptime(self.b_day,"%d/%m/%Y").date()
                if today >= birthdate:
                    years=today.year-birthdate.year
                    print("\n\t************************************************************\n\tYou are {0} years old.".format(years)) 
                    leap_years = [i for i in range(birthdate.year,today.year+1) if i % 4 == 0]
                    ele = len(leap_years)
                    if ele == 0:
                        print("\tSorry, There are no any leap years.")
                    else:
                        print("\tThere are total {0} leap year(s) from your date of birth.\n\tAnd is/are as follows: ".format(len(leap_years)))
                        list_of_leapyear(ele,leap_years)
                    print("\t************************************************************")
                else:
                    future_date = str(birthdate - today)
                    days = future_date.split()
                    print("\n\t************************************************************\n\tToday's date is {0}.\n\tPlease wait for {1} days to reach {2} date.\n\t************************************************************".format(today,days[0],birthdate))            
            except Exception:
                print("""\n\t\t\t'Error!'\n
*******************************************************************************
Do you facing an error? Try the following solutions:
1. Enter your birthday in the format DD/MM/YYYY.
2. The date and month must be between '01 to 31' and '01 to 12', respectively.
3. The year must be between '0001 and 9999'.
4. Only integers should be used.
*******************************************************************************""")
            finally:
                input("\nPress 'Enter' to continue: ")
    x = leap_year_count(input("Enter your Date of Birth in DD/MM/YYYY ? : "))
    x.year()
