"""
Uses the gspread to upload offline conversions from a table in the warehouse for Adwords offline conversion
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# https://tableau.github.io/server-client-python/docs/
# https://community.tableau.com/thread/280748
# https://www.youtube.com/watch?v=knA1DIoAUYI
# def tableau_sheet():
# pip install tabpy-client


# use creds to create a client to interact with the google drive API
def google_sheets(sheet_name):
    # Find a workbook by name and open the first sheet
    try:
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('google_sheet_upload.json', scope)

        client = gspread.authorize(creds)

        if creds.access_token_expired:
            client.login()  # refreshes the token
        workbook = client.open(sheet_name)
        return workbook
    except Exception as e:
        print("Could not connect to google sheet %s") % e


workbook = google_sheets("Offline Conversion Upload - Google & FB Ads - DON'T DELETE")

# Extract and print all of the values
if workbook:
    sheet = workbook.sheet1
    rows = sheet.get_all_records()
    print(rows)
    print("there are " + str(sheet.row_count) + " rows in the sheet.")
    header_row = sheet.row_values(1)
    # clean out worksheet
    sheet.clear()

    # resize worksheet
    sheet.resize(rows=15)

    # we would have tableau from a call to that db, but for now faking it as first 15 of existing table
    for i in range(15):
        index = i+1
        new_row = list(rows[index].values())
        sheet.insert_row(new_row, index)

    sheet.insert_row(header_row, 1)
    print("appended a row, there are " + str(sheet.row_count) + " rows now.")
