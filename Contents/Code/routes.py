from menus_service import MenusService
from helpers import get_player_api, Thumb
from constants import PREFIX

@route(PREFIX + '/livetvcategory', category_id = int)
def LiveTVCategory(category_id):
    palyer_api = get_player_api()
    streams = palyer_api.get_live_streams(category_id)
    oc = ObjectContainer()
    for stream in streams:
        id = str(stream['stream_id'])
        oc.add(CreateVideoClipObject(id=id, title=stream['name'], thumb=stream['stream_icon'], stream_type='live'))
    return oc

@route(PREFIX + '/vodcategory', category_id = int)
def VodCategory(category_id):
    palyer_api = get_player_api()
    streams = palyer_api.get_vod_streams(category_id)
    oc = ObjectContainer()
    for stream in streams:
        id = str(stream['stream_id'])
        oc.add(CreateVideoClipObject(id=id, title=stream['name'], thumb=stream['stream_icon'], stream_type='vod'))
    return oc

@route(PREFIX + '/createvideoclipobject')
def CreateVideoClipObject(id, title, thumb, stream_type):
    palyer_api = get_player_api()
    url = palyer_api.get_url(id, stream_type)
    vco = VideoClipObject(
        # key=Callback(PlayVideo, id=id),
        url = url,
        title = title,
        thumb = Thumb(thumb),
        items = [
            MediaObject(
                parts = [
                    PartObject(
                        key = HTTPLiveStreamURL(url = url)
                    )
                ]
            )
        ]
    )
    return vco

# @indirect
# @route(PREFIX + '/playvideo.m3u8', id)
# def PlayVideo(id):
#     palyer_api = get_player_api()
#     url = palyer_api.get_live_stream_url(id)
#     return IndirectResponse(VideoClipObject, key = url)

@route(PREFIX + '/live_tv')
def LiveTV():
    return MenusService().LiveTV(LiveTVCategory)

@route(PREFIX + '/vod')
def VOD():
    return MenusService().VOD(VodCategory)

@route(PREFIX + '/series')
def Series():
    return MenusService().Series()

