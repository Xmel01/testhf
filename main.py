# from atlassian import Confluence
# from bs4 import BeautifulSoup as bs
#
# confluence = Confluence(
#     url='https://confluence.hflabs.ru/',
# )
#
# head_mas = []
# body_mas = []
#
# page_body = confluence.get_page_by_id(1181220999, "space,body.view,version,container")
# soup = bs(page_body['body']['view']['value'], features="html.parser")
#
# for strs in soup.find_all('th'):
#     head_mas.append(strs.text)
#
# table_head = {n+1: head_mas[n] for n in range(len(head_mas))}
#
# for strs in soup.find_all(['td','ul']):
#     body_mas.append(strs.text)
#
# table_body = {body_mas[n]:body_mas[n+1] for n in range(0, len(body_mas), 2) if n + 1 < len(body_mas)}

# from googleapiclient.discovery import build
#
# service = build('docs', 'v1', developerKey="AIzaSyBp0G31_5aCAiATlIA9kNUL7XpeRsNXF9Q")
# service.close()

# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
#
# scope = ["https://www.googleapis.com/auth/documents"]
# creds = ServiceAccountCredentials.from_json_keyfile_name('google.json', scope)
# client = gspread.authorize(creds)
#
# doc = client.open("УП")
# data = doc.get_all_records()
# print(data)

from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from googleapiclient.discovery import build
import pprint
import io

pp = pprint.PrettyPrinter(indent=4)

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'google-web.json'


credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

r = service.files().list(pageSize=10,
                                fields="nextPageToken, files(id, name, mimeType)").execute()

file_metadata = {
                'name': "name",
            }

#r = service.files().create(body=file_metadata, fields='id').execute()
pp.pprint(r)