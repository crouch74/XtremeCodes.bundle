import urllib, json

class PlayerAPI():
    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password
    
    def get_live_categories(self):
        return self.get_player_api_request('get_live_categories')
    
    def get_live_streams(self, category_id=0):
        params = {'category_id': category_id} if category_id else {}
        return self.get_player_api_request('get_live_streams', params)

    
    def get_vod_categories(self):
        return self.get_player_api_request('get_vod_categories')
    
    def get_vod_streams(self, category_id=0):
        params = {'category_id': category_id} if category_id else {}
        return self.get_player_api_request('get_vod_streams', params)

    def get_series_info(self, series_id):
        params = {'series_id': series_id}
        return self.get_player_api_request('get_series_info', params)

    def get_series_categories(self):
        return self.get_player_api_request('get_series_categories')

    def get_series_streams(self, category_id=0):
        params = {'category_id': category_id} if category_id else {}
        return self.get_player_api_request('get_series', params)
    
    def get_player_api_request(self, action, params={}):
        params = params if(params) else {}
        url = "{}/player_api.php?username={}&password={}&action={}".format(self.server, self.username, self.password, action)
        for k,v in params.items():
            url += "&{}={}".format(k,v)
        print 'url', url
        response = urllib.urlopen(url)
        return json.loads(response.read())

    def get_live_stream_url(self, id):
        return '{}/live/{}/{}/{}.ts'.format(self.server, self.username, self.password, id)
