
from . import utils

# load dictionary from the file using the utils
# then process the file
def load_categories(path):
    loaded_dic = utils.read_dictionary_file(path=path)
    inv_dic = {}
    for key in loaded_dic.keys():
        data = loaded_dic[key]
        tags = [val.strip().upper() for val in data.split(",")]
        for tag in tags:
            inv_dic[tag] = key
            #if len(tag) > 0 and tag[0] == "$":
            #    print(tag)
    
    """
    for key in inv_dic.keys():
        if key[0] == "$":
            print("{} : {}".format(key, inv_dic[key]))
            new_key = key[1:]
            print(new_key)
            for _key in inv_dic.keys():
                if inv_dic[_key].upper() == new_key:
                    print("to update {} : {} -> {}".format(_key, inv_dic[_key], inv_dic[key]))
    """

    return inv_dic


class TITSCategories:

    def __init__(self, path) -> None:
        self.categories = load_categories(path)
    
    def get_category(self, key):
        return self.categories[key] if key in self.categories else "OTHER"
        