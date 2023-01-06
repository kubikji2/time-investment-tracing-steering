from collections import defaultdict
from datetime import timedelta


from . import calendar
from . import categories

class TITSTimeInvestment:

    def __init__(self, calendars : list, categories : categories.TITSCategories) -> None:
        self.calendars = calendars
        self.categories = categories
        self.process_calendars()
    
    def process_calendars(self):
        self.category_bins = defaultdict(lambda : list())
        self.activity_bins = defaultdict(lambda : list())
        for calendar in self.calendars:
            self.process_calendar(calendar)
    
    def process_calendar(self, calendar : calendar.TITSCalendar):
        for ev in calendar.events:
            key = self.categories.get_category(ev.tag)
            ev.category = key
            self.category_bins[key].append(ev)
            self.activity_bins[ev.activity].append(ev)
    
    def print_time_investment(self):
        self.print_category_summary()
        self.print_activity_summary()
    
    def print_category_summary(self):
        for key in self.category_bins:
            l = self.category_bins[key]
            tags = defaultdict(lambda : timedelta() )
            tt = timedelta()
            for el in l:
                dur = el.get_duration()
                tt += dur
                tags[el.tag] += dur
            print("{}:\t{}".format(key, tt))
            for tk in tags:
                print(" '-> {}:\t{}".format(tk,tags[tk]))
        pass
    
    def print_activity_summary(self):
        pass