
from .icream.icream import event

class TITSEvent(event.ICREAMEvent):

    def __init__(self, tag, activity="", ev : event.ICREAMEvent = None, start=None, end=None, name="", organizer="", description="", component=None):
        if ev is not None:
            start = ev.start
            end = ev.end
            name = ev.name
            organizer = ev.organizer
            description = ev.description
            component = ev.component
        super().__init__(start, end, name, organizer, description, component)
        self.tag = tag
        self.activity = activity
        self.category = None
