from player_api import PlayerAPI

def Thumb(url):
    Resource.ContentsOfURLWithFallback(url.replace(' ', '%20'))

def get_player_api():
    return PlayerAPI(Prefs['server'], Prefs['username'], Prefs['password'])
