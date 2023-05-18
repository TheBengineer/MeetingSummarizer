import pandas as pd
import datetime as dt
import win32com.client


def get_appointments(calendar, subject_kw=None, exclude_subject_kw=None, body_kw=None):
    if subject_kw == None:
        appointments = [app for app in calendar]
    else:
        appointments = [app for app in calendar if subject_kw in app.subject]

    if exclude_subject_kw != None:
        appointments = [app for app in appointments if exclude_subject_kw not in app.subject]
    cal_subject = [app.subject for app in appointments]
    cal_start = [app.start for app in appointments]
    cal_end = [app.end for app in appointments]
    cal_body = [app.body for app in appointments]

    df = pd.DataFrame({'subject': cal_subject,
                       'start': cal_start,
                       'end': cal_end,
                       'body': cal_body})
    return df


def get_calendar(begin, end):
    outlook = win32com.client.Dispatch('Outlook.Application').GetNamespace('MAPI')
    calendar = outlook.getDefaultFolder(9).Items
    calendar.IncludeRecurrences = True
    calendar.Sort('[Start]')

    restriction = "[Start] >= '" + begin.strftime('%m/%d/%Y') + "' AND [END] <= '" + end.strftime('%m/%d/%Y') + "'"
    calendar = calendar.Restrict(restriction)
    return calendar


cal = get_calendar(dt.datetime(2020, 1, 1), dt.datetime(2020, 7, 31))
