from collections import defaultdict
from datetime import timedelta
import datetime

from . import calendar
from . import categories

class TITSTimeInvestment:

    def __init__(self, calendars : list, categories : categories.TITSCategories) -> None:
        self.calendars = calendars
        self.categories = categories
        self.process_calendars()


    # prepare vars and process all calendars    
    def process_calendars(self):
        self.category_bins = defaultdict(lambda : list())
        self.activity_bins = defaultdict(lambda : list())
        for calendar in self.calendars:
            self.process_calendar(calendar)
    

    # process a single calendar
    def process_calendar(self, calendar : calendar.TITSCalendar):
        for ev in calendar.events:
            key = self.categories.get_category(ev.tag)
            ev.category = key
            self.category_bins[key].append(ev)
            self.activity_bins[ev.activity].append(ev)
    

    # prints time investement for given time interval:
    # 'startime_datetime' variable defines the start datetime 
    # 'end_datetime' variable defines the end datetime
    # 'ignore_long_events' defines whether events over one day should be skipped
    def print_time_investment(self, start_datetime : datetime.datetime = None, end_datetime : datetime.datetime = None, ignore_long_events : bool = False):
        
        # prints the time durations by the main category
        self.print_category_summary(start_datetime, end_datetime, ignore_long_events)
        # prints the time durations by the associated activity
        self.print_activity_summary(start_datetime, end_datetime, ignore_long_events)
    

    # for each category the total time spent doing it is printed
    # the same is done for the subcategories 
    def print_category_summary(self, start_datetime : datetime.datetime = None, end_datetime : datetime.datetime = None, ignore_long_events : bool = False):

        # iterate over category bins
        for key in self.category_bins:
            l = self.category_bins[key]
            tags = defaultdict(lambda : timedelta() )
            tt = datetime.timedelta()
            # iterate over the list inside the bin
            for el in l:
                # count the category in iff the event fits the conditions
                if (start_datetime is None or el.start > start_datetime) and (end_datetime is None or el.end < end_datetime) and (not ignore_long_events or el.get_duration() < datetime.timedelta(days=1)):
                    dur = el.get_duration()
                    tt += dur
                    tags[el.tag] += dur
            # print the category and total duration
            print(("{}\n{}").format(key.upper(), tt))

            # print tags for each category
            for tk in tags:
                print("'-> {}: {}".format(tags[tk], tk))
            print()
    
    # for each activity the total time spent doing it is printed
    def print_activity_summary(self, start_datetime : datetime.datetime = None, end_datetime : datetime.datetime = None, ignore_long_events : bool = False):
        # TODO this
        pass