def Thumb(url):
    try:
        data = HTTP.Request(url, cacheTime = CACHE_1MONTH).content
        return DataObject(data, 'image/jpeg')
    except:
        return Redirect(R(ICON))