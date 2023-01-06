
from . import utils

def load_categories(path):
    loaded_dic = utils.read_dictionary_file(path=path)
    inv_dic = {}
    for key in loaded_dic.keys():
        data = loaded_dic[key]
        tags = [val.strip().upper() for val in data.split(",")]
        for tag in tags:
            inv_dic[tag] = key
    return inv_dic


class TITSCategories:

    def __init__(self, path) -> None:
        self.categories = load_categories(path)
    
    def get_category(self, key):
        return self.categories[key] if key in self.categories else "OTHER"
        