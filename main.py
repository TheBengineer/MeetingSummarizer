import os
import csv
import datetime


def load_calendar_csv(filename):
    project_dir = os.getcwd()
    filepath = os.path.join(project_dir, filename)
    if os.path.isfile(filepath):
        with open(filepath, 'r', encoding="utf-8-sig", errors="ignore") as csvfile:
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


def format_event(event, format_str):
    event_name = event['Subject']
    event_date = event['Start Date']
    event_date_string = datetime.datetime.strptime(event_date, '%m/%d/%Y').strftime('%A, %B %d')
    return format_str.format(event_name=event_name, event_date_string=event_date_string)


def load_template_string():
    project_dir = os.getcwd()
    filepath = os.path.join(project_dir, 'template.txt')
    if os.path.isfile(filepath):
        with open(filepath, 'r') as template_file:
            return template_file.read()


def process_events(events):
    """
    loops through events and formats descriptions for priting
    """
    for event in events:
        event_str_formatted = format_event(event, template_str)
        print(event_str_formatted)


if __name__ == "__main__":
    template_str = load_template_string()
    all_events = load_calendar_csv('calendar.csv')
    events_this_week = filter_events(all_events)
    process_events(events_this_week)
