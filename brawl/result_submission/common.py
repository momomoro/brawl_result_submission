from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# Replace this with the sheet ID of the current season, this is season 3 - https://docs.google.com/spreadsheets/d/1PE--nKhUeAoiLbtRG-K1797nPqSy75jTa6iJjJpRj7s/edit#gid=249978244
SHEET_ID = '1PE--nKhUeAoiLbtRG-K1797nPqSy75jTa6iJjJpRj7s'
RANGE = 'A1:AV4'


def get_sheet(sheet_id, range):
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id, range=range).execute()
    return result


def get_players(sheet):
    players = sheet[0]
    players = list(filter(None, players))
    return players


def generate_decks(sheet):
    decks = {}
    players = sheet[0]
    commanders = sheet[3]
    players = list(filter(None, players))
    deck_number = 0
    for player in players:
        decks[player] = []
        for commander in commanders[deck_number:]:
            deck_number += 1
            decks[player].append(commander)
            if deck_number % 4 == 0:
                break
    return decks
