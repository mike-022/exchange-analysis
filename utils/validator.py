import datetime
def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except:
        print("Incorrect data format, should be YYYY-MM-DD")
        return False


def validatedate(start, end):
    if end < start:
        print("Start date must come before end.")
        return False
    else:
        return True