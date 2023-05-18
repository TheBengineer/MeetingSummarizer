import os
import csv


def load_calendar_csv(filename):
    project_dir = os.getcwd()
    filepath = os.path.join(project_dir, filename)
    if os.path.isfile(filepath):
        with open(filepath, 'r', encoding="windows-1252", errors="ignore") as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)


data = load_calendar_csv('calendar.csv')
