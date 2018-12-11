import pprint
import sys

import spotipy
import spotipy.util as util
import simplejson as json
import pprint



# name = 'manchester orchestra'
# spotify = spotipy.Spotify()
# results = spotify.search(q='artist:' + name, type='artist')

# print results

username = 'bheltzel'

scope = 'user-top-read'
token = util.prompt_for_user_token(username,scope,client_id='9c7e3fd10710461b8127423dbfcecf47',client_secret='11317452a28e4364863fbf87572d8905',redirect_uri='http://localhost/')

# token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    ranges = ['short_term', 'medium_term', 'long_term']
    for range in ranges:
        print "range:", range
        results = sp.current_user_top_tracks(time_range=range, limit=50)
        # for i, item in enumerate(results['items']):
            
            # print i, item['name'], '//', item['artists'][0]['name']
        # print
        print(results['items'])
        
else:
    print("Can't get token for", username)