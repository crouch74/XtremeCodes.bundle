from player_api import PlayerAPI
from menu_handlers import MenuHandlers
from constants import PREFIX, ART, NAME

PLAYER_API = None 
MENU_HANDLERS = None 

def Start():
    Log('Start called')

    Plugin.AddViewGroup("List", viewMode="List", mediaType="items") 
    Log('Added view group')

    ObjectContainer.title1 = NAME
    ObjectContainer.view_group = 'List'
    ObjectContainer.art = R(ART)
    DirectoryObject.thumb = R(ART)
    DirectoryObject.art = R(ART)
    InputDirectoryObject.thumb = R(ART)
    InputDirectoryObject.art = R(ART)
    VideoClipObject.thumb = R(ART)
    VideoClipObject.art = R(ART)

    Log('Added Defaults')

    PLAYER_API = PlayerAPI(Prefs['server'], Prefs['username'], Prefs['password'])
    MENU_HANDLERS = MenuHandlers(PLAYER_API)

@handler(PREFIX, NAME)
def MainMenu():
    Log('Main menu started')

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
    Log('created mainmenu list')
    oc = ObjectContainer()
    Log('created OC')
    for item in main_menu:
        oc.add(DirectoryObject(
            key = Callback(item['callback']),
            title = item.tv
        ))

    Log('Filled oC')
    return oc

@route(PREFIX + '/live_tv')
def LiveTV():
    return MENU_HANDLERS.LiveTV()

@route(PREFIX + '/vod')
def VOD():
    return MENU_HANDLERS.VOD()

@route(PREFIX + '/series')
def Series():
    return MENU_HANDLERS.Series()