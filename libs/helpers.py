import sys
from pprint import pprint

from jinja2 import Template


def prep_template(template_path: str) -> Template:
    """Read template

    Returns:
        Template: Template object
    """
    with open(template_path, "r") as f:
        template = Template(f.read())
    return template


def is_send(emails: list) -> None:
    """Prints email list to user and asks for prompt to proceed

    Args:
        emails (list): list of emails to print
    """
    pprint(emails)
    print(f"Do you want to send email to {len(emails)} groups?")
    yes = {"yes", "y", "ye", ""}
    no = {"no", "n"}
    choice = input().lower()
    if choice in yes:
        return
    elif choice in no:
        sys.exit(2)
    else:
        sys.stdout.write("Please respond with 'yes' or 'no'")
