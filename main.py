import os
import csv
import datetime


def load_calendar_csv(filename):
    project_dir = os.getcwd()
    filepath = os.path.join(project_dir, filename)
    if os.path.isfile(filepath):
        with open(filepath, 'r', encoding="windows-1252", errors="ignore") as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)


def get_current_week():
    today = datetime.date.today()
    return today.isocalendar()[1]


def start_date_is_this_week(start_date_str):
    start_date = datetime.datetime.strptime(start_date_str, '%m/%d/%Y').date()
    return start_date.isocalendar()[1] == get_current_week()


def filter_events(events):
    return [event for event in events if start_date_is_this_week(event['Start Date'])]


all_events = load_calendar_csv('calendar.csv')
events_this_week = filter_events(all_events)
print(events_this_week)