from googleapiclient.discovery import build


def get_edm_list(service: build, sheet_id: str, sheet_name: str) -> list:
    """_summary_

    Args:
        service (build): handler
        sheet_id (str): google_sheet id with emails

    Returns:
        list: list of emails
    """
    data = []
    # Call the Sheets API
    request = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=sheet_id, range=sheet_name, majorDimension="ROWS")
    )
    response = request.execute()
    # return response["values"]
    for row in response["values"]:
        data.append(dict(zip(["name", "last_name", "email", "cc"], row)))
    return data
