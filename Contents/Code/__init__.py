from constants import PREFIX, ART, NAME
from routes import LiveTV, VOD, Series, LiveTVCategory, VodCategory
from helpers import Thumb, get_player_api

def Start():

    Plugin.AddViewGroup("List", viewMode="List", mediaType="items") 

    ObjectContainer.title1 = NAME
    ObjectContainer.view_group = 'List'
    ObjectContainer.art = R(ART)
    DirectoryObject.thumb = R(ART)
    DirectoryObject.art = R(ART)
    InputDirectoryObject.thumb = R(ART)
    InputDirectoryObject.art = R(ART)
    VideoClipObject.thumb = R(ART)
    VideoClipObject.art = R(ART)

@handler(PREFIX, NAME)
def MainMenu():

    main_menu = [{
        'title': 'LIVE TV',
        'callback': LiveTV
    }, {
        'title': 'Video on Demand',
        'callback': VOD
    }, {
        'title': 'Series',
        'callback': Series
    }]
    oc = ObjectContainer()
    for item in main_menu:
        oc.add(DirectoryObject(
            key = Callback(item['callback']),
            title = item['title']
        ))

    return oc