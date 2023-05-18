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


def sort_events_oldest_first(events):
    return sorted(events, key=lambda event: datetime.datetime.strptime(event['Start Date'], '%m/%d/%Y').date())


def filter_events(events):
    filtered = [event for event in events if start_date_is_this_week(event['Start Date'])]
    sorted_events = sort_events_oldest_first(filtered)
    return sorted_events


def format_event_description(event_description):
    return event_description


def process_events(events):
    """
    loops through events and formats descriptions for priting
    """
    for event in events:
        event['Description'] = format_event_description(event['Description'])

    return events


all_events = load_calendar_csv('calendar.csv')
events_this_week = filter_events(all_events)
print(events_this_week)
