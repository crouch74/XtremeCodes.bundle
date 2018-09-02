from helpers import Thumb
from constants import PREFIX, ART, NAME

class MenuHandlers():
    def __init__(self, player_api):
        self.player_api = player_api
    
    def LiveTV(self):
        categories = self.player_api.get_live_categories()
        oc = ObjectContainer()
        for category in categories:
            oc.add(DirectoryObject(
                key = Callback(LiveTVCategory, category_id = category.category_id),
                title = category.category_name
            ))
        return oc
    
    @route(PREFIX + '/live_tv_category', category_id = int)
    def LiveTVCategory(category_id):
        streams = self.player_api.get_live_streams(category_id)
        oc = ObjectContainer()
        for stream in streams:
            oc.add(VideoClipObject(
                url = self.player_api.get_live_stream_url(stream.stream_id),
                title = stream.name,
                thumb = Callback(Thumb, url=stream.stream_icon)
            ))
        return oc

    def VOD(self):
        categories = self.player_api.get_vod_categories()
        oc = ObjectContainer()
        for category in categories:
            oc.add(DirectoryObject(
                title = category.category_name
            ))
        return oc

    def Series(self):
        categories = self.player_api.get_series_categories()
        oc = ObjectContainer()
        for category in categories:
            oc.add(DirectoryObject(
                title = category.category_name
            ))
        return oc