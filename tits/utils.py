from .icream.icream import event

def is_parsable_event(ev : event.ICREAMEvent):
    return "[" in ev.name and "]" in ev.name

def parse_event(ev : event.ICREAMEvent):

    tag = ""
    activity = ""

    if is_parsable_event(ev):
        # string work piece
        swp = ev.name.split("[")[1]
        swp, description = swp.split("]")
        if "-" in swp:
            tag, activity = swp.split("-")[0:2]
        else:
            tag = swp
        tag = tag.strip().upper()
        activity = activity.strip().upper()

    return tag, activity

def read_dictionary_file(path) -> dict :
    dic = {}
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if not "#" in line and ":" in line:
                key, data = line.split(":")
                key = key.strip()
                data = data.strip()
                dic[key] = data
    return dic
    