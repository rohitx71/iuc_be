from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

scopes = ["https://www.googleapis.com/auth/drive",
          "https://www.googleapis.com/auth/spreadsheets"]

secret_file = os.path.join(os.getcwd(), 'credentials.json')

# # If modifying these scopes, delete the file credentials.json.
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
#           'https://www.googleapis.com/auth/drive',
#           ]


def init():
    """Initializes GCP for the scopes defined.
    """
    # creds = None
    # # The file credentials.json stores the user's access and refresh tokens, and is
    # # created automatically when the authorization flow completes for the first
    # # time.
    # if os.path.exists('/token.json'):
    #     creds = service_account.Credentials.from_service_account_file('/Users/rohitsingh/Documents/Projects/IUC/FormSubmission/token.json', scopes=SCOPES)
    # # If there are no (valid) credentials available, let the user log in.
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow = service_account.In InstalledAppFlow.from(
    #             '/Users/rohitsingh/Documents/Projects/IUC/FormSubmission/credentials.json', SCOPES)
    #         creds = flow.run_local_server(port=0)
    #     # Save the credentials for the next run
    #     with open('/Users/rohitsingh/Documents/Projects/IUC/FormSubmission/token.json', 'w') as token:
    #         token.write(creds.to_json())
    credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
    sheets_service = build('sheets', 'v4', credentials=credentials)
    drive_service = build('drive', 'v3', credentials=credentials)
    return sheets_service, drive_service



