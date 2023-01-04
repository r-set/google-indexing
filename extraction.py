from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json

#add site url
url = ''
 
#add json_key
JSON_KEY_FILE = ""
 
SCOPES = [ "https://www.googleapis.com/auth/indexing" ]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
 
 
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)
http = credentials.authorize(httplib2.Http())
 

print(url)
content = {}
content['url'] = url
content['type'] = "URL_UPDATED"
json_content = json.dumps(content)
 
 
response, content = http.request(ENDPOINT, method="POST", body=json_content)
result = json.loads(content.decode())