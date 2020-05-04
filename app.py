import sys
from datetime import date

import spotipy
import spotipy.util as util
import simplejson as json

username = 'bheltzel'

scope = 'user-top-read'
token = util.prompt_for_user_token(username,scope,client_id='9c7e3fd10710461b8127423dbfcecf47',client_secret='11317452a28e4364863fbf87572d8905',redirect_uri='http://localhost/')

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    ranges = ['short_term', 'medium_term', 'long_term']
    with open('csv.csv', 'w') as f: # change to 'a' to append
      for rng in ranges:
          results = sp.current_user_top_tracks(time_range=rng, limit=50)
          for i, item in enumerate(results['items']):
              csv = str(i) 
              csv += ',"' + username
              csv += '","' + item['name'].encode("utf-8") 
              csv += '","' + item['artists'][0]['name'].encode("utf-8")
              csv += '",' + str(date.today())
              csv += ',' + rng + '\n'
              f.write(csv)
      
    # TODO: write CSV to mysql
else:
    print("Can't get token for", username)