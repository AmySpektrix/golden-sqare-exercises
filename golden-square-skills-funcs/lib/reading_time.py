import datetime

def reading_time(text,wpm):
    if text == "":
        raise Exception("No Text Provided!")
    number_of_minutes = (len(text.split()))/wpm
    time_format= datetime.timedelta(minutes = round(number_of_minutes,1))
    return f"approx. {time_format}"