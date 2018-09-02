from player_api import PlayerAPI
from menu_handlers import MenuHandlers

NAME = 'XTREMECODES'
PREFIX = '/video/' + NAME.lower()
PLAYER_API = PlayerAPI(Prefs['server'], Prefs['username'], Prefs['password']); 
MENU_HANDLERS = MenuHandlers(PLAYER_API)
ART = 'art-default.jpg'
ObjectContainer.view_group = 'List'
ObjectContainer.art = R(ART)

def Start():
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items") 

    ObjectContainer.title1 = NAME

@handler(PREFIX, NAME)
def MainMenu():
    main_menu = [{
        title: 'LIVE TV',
        callback: LiveTV
    }, {
        title: 'Video on Demand',
        callback: VOD
    }, {
        title: 'Series',
        callback: Series
    }]
    oc = ObjectContainer()
    for item in main_menu:
        oc.add(DirectoryObject(
            key = Callback(item.callback),
            title = item.tv
        ))
    
    return oc

@route(PREFIX + '/live_tv')
def LiveTV():
    return MENU_HANDLERS.LiveTV()

@handler(PREFIX + '/vod')
def VOD():
    return MENU_HANDLERS.VOD()

@handler(PREFIX + '/series')
def Series():
    return MENU_HANDLERS.Series()