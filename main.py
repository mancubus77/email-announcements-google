# Base libs
import base64
from pathlib import Path
from pprint import pprint

# Python libs
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email.utils import formataddr
from requests import HTTPError
from jinja2 import Template

# Project libs
from libs.arg_parser import parse_args
from libs.auth import oAuth, get_service
from libs.get_edm import get_edm_list
from libs.helpers import prep_template
from libs.helpers import is_send
from libs.configs import Config

# from config import SPREADSHEET_ID, SPREADSHEET_TAB, SUBJ, CREDS_PATH, TEMPLATE


def send_email(service: build, template: Template, context: dict):
    """Send email via GMail

    Args:
        service (build): oAuth handler
        email (str): email address of the person to send
    """
    email_payload = template.render(context)
    message = MIMEText(email_payload, "html")
    message["to"] = context["email"]
    message["subject"] = config.subj
    if "cc" in context:
        message["cc"] = context["cc"]
    create_message = {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode()}

    try:
        message = (
            service.users().messages().send(userId="me", body=create_message).execute()
        )
        print(f'sent message to {message} Message Id: {message["id"]}')
    except HTTPError as error:
        print(f"An error occurred: {error}")
        message = None


if __name__ == "__main__":
    args = parse_args()
    config = Config(args.config_path)
    oAuth = oAuth(creds_path=config.creds_path)
    sheet_service = get_service("sheets", oAuth)
    email_service = get_service("gmail", oAuth)
    email_template = prep_template(config.template)
    emails = get_edm_list(sheet_service, config.spreadsheet_id, config.spreadsheet_tab)
    is_send(emails)
    for email in emails:
        send_email(email_service, email_template, email)
