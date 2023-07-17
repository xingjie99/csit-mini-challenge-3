from datetime import datetime

# check if ISO date format (YYYY-MM-DD)
def verify_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except:
        return False
    
# check if end_date is more than or equal to start_date
def is_date_greater_or_equal(start_date, end_date):
    return datetime.strptime(end_date, "%Y-%m-%d") >= datetime.strptime(start_date, "%Y-%m-%d")


def convert_to_datetime(date_string):
    return datetime.fromisoformat(date_string)


def get_number_of_days(start_date, end_date):
    difference = (end_date - start_date).days
    # add 1 day to account for inclusive
    return difference + 1