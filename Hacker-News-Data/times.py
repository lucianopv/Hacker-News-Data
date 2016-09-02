import read
import pandas as pd
import dateutil

def hours(row):
    return dateutil.parser.parse(row["submission_time"]).hour
   
def months(row):
    return dateutil.parser.parse(row["submission_time"]).month
    
def days(row):
    return dateutil.parser.parse(row["submission_time"]).day
    
def years(row):
    return dateutil.parser.parse(row["submission_time"]).year
    
def minutes(row):
    return dateutil.parser.parse(row["submission_time"]).minute
   
    
def times(x):
    df = read.load_data()
    df["submission_hour"] = df.apply(hours, axis=1)
    df["submission_month"] = df.apply(months, axis=1)
    df["submission_day"] = df.apply(days, axis=1)
    df["submission_year"] = df.apply(years, axis=1)
    df["submission_minute"] = df.apply(minutes, axis=1)
    if x == "hour" or x == "hours":
        return df["submission_hour"].value_counts()
    elif x == "day" or x == "days":
        return df["submission_day"].value_counts()
    elif x == "year" or x == "years":
        return df["submission_year"].value_counts()
    elif x == "month" or x == "months":
        return df["submission_month"].value_counts()
    elif x == "minute" or x == "minutes":
        return df["submission_minute"].value_counts()
        
print(times("month"))