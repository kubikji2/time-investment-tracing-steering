from tits.icream.icream import calendar as ic
from tits import utils
from tits import calendar as tc
from tits import categories
from tits import time_investment as ti

import datetime

if __name__=="__main__":
    # dummy path
    _path = "./kubikji2@fel.cvut.cz.ics"
    tits_cal = tc.TITSCalendar(path=_path)
    tits_cal.sort_calendar_by_date()
    #tits_cal.print_calendar()
    tits_cat = categories.TITSCategories("./categories.tcf")

    tits_ti = ti.TITSTimeInvestment([tits_cal], tits_cat)

    _start = datetime.datetime(2023,3,20,0,0,0, tzinfo=datetime.timezone(datetime.timedelta(0,0,0,0,0,1)))
    _end = datetime.datetime(2023,3,27,0,0,0, tzinfo=datetime.timezone(datetime.timedelta(0,0,0,0,0,1)))
    tits_ti.print_time_investment(_start, _end, True)
    
    #for ev in tits_ti.events:
    #    tag, activity = utils.parse_event(ev)
    #    print(tag, activity)

    
