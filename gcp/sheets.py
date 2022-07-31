from __future__ import print_function

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1IfVzsIs7Fs2Cjzck2ISoAZBvUjlNJw_opcI7naQbvMU'
SAMPLE_RANGE_NAME = 'Sheet1!A:G'


def append_values(service, values):
    # [START sheets_append_values]
    # values = [
    #     [
    #         "1Fifty",
    #         "Sixty",
    #         "Seventy",
    #         "Eighty",
    #     ],
    # ]
    # [START_EXCLUDE silent]
    # values = _values
    # [END_EXCLUDE]
    body = {
        'values': [values]
    }
    result = service.spreadsheets().values().append(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME,
        valueInputOption="RAW", body=body).execute()
    print('{0} cells appended.'.format(result
                                       .get('updates')
                                       .get('updatedCells')))
    # [END sheets_append_values]
    return result

if __name__ == "__main__":
    append_values()
