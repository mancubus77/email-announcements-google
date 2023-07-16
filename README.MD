# Email Announcements Automation tool

This project was created to address frustrations with EDM (Electronic Direct Mail) marketing tools. While these tools are great, sometimes people tend to ignore emails as they perceive them as marketing rubbish. When an EDM is sent, all users receive individual emails without realizing who else received it within their company or organization. This tool allows you to send batch emails to groups of people, making the emails appear more natural and as if they were sent from your own mailbox.

For example, let's say you have three teams that you would like to announce a new feature to. Instead of emailing them individually, this tool can send three emails to groups of people visible in the "TO" and "CC" fields. This creates a more person-to-person communication and encourages recipients to reply, as the email appears to be from you. However, it's important to note that this tool won't help you generate leads or receive good responses if you don't already have a certain level of trust with your customers/leads. It's simply an automation tool that extends your smart mind.

## How it works

<p align="center">
<img height="400" src="./doc/images/mail-sender.png">
</p>

The script utilizes the following Google APIs:

- Gmail
- Google Drive
- Google Sheets

Therefore, you need to download a Google OAuth token from the Google Console and save it in the google-creds folder.

**First**, create a Google Sheet with the emails of the people you would like to interact with. For instance, it may look like this:

<p align="center">
<img height="400" src="./doc/images/google-sheet-edm.png">
</p>

| Column | Description                                        |
| :----: | :------------------------------------------------- |
|   A    | Name of the team or name (used for Jinja template) |
|   B    | Last name (if needed)                              |
|   C    | Comma-separated list of recipients (TO)            |
|   D    | Comma-separated list of recipients (CC)            |
|  |

**Second** Prepare Jinja template what for EDM. Default is HTML and save it announcements folder.

**Third** Update configuration file

```PYTHON
# Google Spreadseet ID with emails
SPREADSHEET_ID = "SoMeThIngLiKeThIs"
# Name of Spreadsheet tab
SPREADSHEET_TAB = "Tabname"
# Email Subject
SUBJ = "G'Day man, Rise and shine!"
# Path to JSON with google oAuth
CREDS_PATH = "google-creds/my-creds.json"
# Template to use
TEMPLATE = "announcements/example.html"
```

`SPREADSHEET_ID` - Google Doc ID, which can be extracted from the document URL. For example, if the Sheet URL is https://docs.google.com/spreadsheets/d/1I8SqlheQ6CEISi6hkbHl0YIFcWCRODg7ng0JSHL4Nio/edit#gid=0, and `1I8SqlheQ6CEISi6hkbHl0YIFcWCRODg7ng0JSHL4Nio` is document ID.

`SPREADSHEET_TAB` - Spreadsheet tab name

`SUBJ` - Subject of EDM (without Jinja)

`CREDS_PATH` - path with google oAuth credentials

`TEMPLATE` - path to email body (Jinja)

You can have multiple configuration files if you want to keep the announcements relevant to certain groups of people. For example, you may not want to send announcements about developer features to infrastructure guys or DevOps.

## Installation

`make install`

or

```<bash>
	python3 -m venv .venv
	source ./.venv/bin/activate
	python3 -m pip install --upgrade pip
	pip install -r requirements.txt
```

## Usage

Simply run the script with the -c parameter, pointing to the configuration file.

```
❯ python main.py -h
usage: main.py [-h] -c FILE

Config file

options:
  -h, --help            show this help message and exit
  -c FILE, --config FILE
                        path to config file
```

Run with the `test.py` config:

```
❯ python main.py -c configs/test.py
Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=000000-<skip...skip...skip>
```

After run, you will be redirected to Google SignIn page to select account you would like to use

<p align="center">
<img height="400" src="./doc/images/auth.png">
</p>

After successful authorization, the script will print the user groups:

```
[{'cc': 'sales-head@acme.com',
  'email': 'Mr Sales <sales@acme.com>, Mr sales-ops <sales-ops@acme.com>',
  'last_name': 'Sales ',
  'name': 'Team'},
 {'cc': 'tech-head@acme.com',
  'email': 'Mr Tech <tech@acme.com>, John Dow <tech-arch@acme.com>',
  'last_name': 'Tech',
  'name': 'Team'}]
Do you want to send email to 2 groups?
```

If you type "Y" or "Yes," the script will send the emails.
