def is_leap_year(a_year):
    """Determine if a Year is a Leap Year"""
    if a_year%4==0 and not (a_year%100==0 and not a_year%400==0):
        print("True")
    else:
        print("False")

is_leap_year(2016)