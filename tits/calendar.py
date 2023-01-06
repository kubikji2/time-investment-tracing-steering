
from .icream.icream import calendar 
from . import utils
from . import event

class TITSCalendar(calendar.ICREAMCalendar):

    def __init__(self, path=None, calendar=None):
        super().__init__(path, calendar)
        self.process_events(self.events)
    
    def process_events(self, events):
        filtered = []
        for ev in events:
            if utils.is_parsable_event(ev):
                _tag, _category = utils.parse_event(ev)
                _ev = event.TITSEvent(tag=_tag,activity=_category, ev=ev)
                filtered.append(_ev)
            pass
            
        self.events = filtered

