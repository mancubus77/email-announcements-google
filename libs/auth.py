import sys

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from pprint import pprint


SCOPES = [
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive.readonly",
]


def oAuth(creds_path: str):
    """Init oAuth app

    Returns:
        build: oAuth object to address API
    """
    flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
    return flow.run_local_server(port=0)


def get_service(api_type: str, oAuth: build):
    """Get Service handler

    Args:
        api_type (str): type of the handler, eg "sheets", "gmail", "docs", etc
        oAuth (build): _description_

    Returns:
        _type_: Build oject
    """
    if api_type == "sheets":
        return build("sheets", "v4", credentials=oAuth)
    elif api_type == "gmail":
        return build("gmail", "v1", credentials=oAuth)
