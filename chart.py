import mysql.connector
import simplejson as json

cnx = mysql.connector.connect()

cursor = cnx.cursor()

query = ("select rank + 1 as song_rank, song, artist from chart where chart_type = 'medium_term'")

cursor.execute(query)
# for (song_rank, artist, hire_date) in cursor:
row_headers=[x[0] for x in cursor.description] #this will extract row headers
rv = cursor.fetchall()
json_data=[]
for result in rv:
    json_data.append(dict(zip(row_headers,result)))

cursor.close()
cnx.close()

print(json.dumps(json_data)) 