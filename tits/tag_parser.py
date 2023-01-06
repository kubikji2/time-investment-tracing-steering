from icream.icream import event

def parse_event(ev : event.ICREAMEvent):

    tag = ""
    activity = ""

    name = ev.name
    print(name)
    if "[" in name and "]" in name:
        # string work piece
        swp = name.split("[")[1]
        swp, description = swp.split("]")
        if "-" in swp:
            tag, activity = swp.split("-")
        else:
            tag = swp
        tag = tag.strip().upper()
        activity = activity.strip().upper()

    return tag, activity

