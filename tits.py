from tits.icream.icream import calendar as ic
from tits import utils
from tits import calendar as tc
from tits import categories
from tits import time_investment as ti

if __name__=="__main__":
    _path = "./kubikji2@fel.cvut.cz.ics"
    tits_cal = tc.TITSCalendar(path=_path)
    tits_cal.sort_calendar_by_date()
    #tits_cal.print_calendar()
    tits_cat = categories.TITSCategories("./categories.tcf")

    tits_ti = ti.TITSTimeInvestment([tits_cal], tits_cat)
    tits_ti.print_time_investment()
    #for ev in icrm_cal.events:
        #tag, activity = utils.parse_event(ev)
        #print(tag, activity)

    
