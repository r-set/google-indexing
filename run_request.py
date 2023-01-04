from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build 
from googleapiclient.http import BatchHttpRequest
import httplib2
import json

#add url exampe 'https://site.com/index.html':'URL_UPDATED',
requests = {


}

#add json_key
JSON_KEY_FILE = ""
 
SCOPES = [ "https://www.googleapis.com/auth/indexing" ]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
 
#authorize credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)
http = credentials.authorize(httplib2.Http())
 
#build service
service = build('indexing', 'v3', credentials=credentials)
 
def insert_event(request_id, response, exception):
    if exception is not None:
      print(exception)
    else:
      print(response)
 
batch = service.new_batch_http_request(callback=insert_event)
 
for url, api_type in requests.items():
    batch.add(service.urlNotifications().publish(
        body={"url": url, "type": api_type}))
 
batch.execute()