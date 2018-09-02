from helpers import get_player_api
from constants import PREFIX, ART, NAME

class MenusService():
    def __init__(self):
        self.player_api = get_player_api()
    
    def LiveTV(self, LiveTVCategory):
        categories = self.player_api.get_live_categories()
        oc = ObjectContainer()
        for category in categories:
            oc.add(DirectoryObject(
                key = Callback(LiveTVCategory, category_id = category['category_id']),
                title = category['category_name']
            ))
        return oc

    def VOD(self, VodCategory):
        categories = self.player_api.get_vod_categories()
        oc = ObjectContainer()
        for category in categories:
            oc.add(DirectoryObject(
                key = Callback(VodCategory, category_id = category['category_id']),
                title = category['category_name']
            ))
        return oc

    def Series(self):
        categories = self.player_api.get_series_categories()
        oc = ObjectContainer()
        for category in categories:
            oc.add(DirectoryObject(
                title = category['category_name']
            ))
        return oc