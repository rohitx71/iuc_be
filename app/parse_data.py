from gcp.main import gdrive_helper


def parse(event_type, first_name, last_name, email, abstract, file_name, mime_type):

    # create folders in drive

    # upload pdf to drive

    # vimeo

    # append values to sheet
    gdrive_helper(sheets_data=[event_type, first_name, last_name, email],
                  folder="iuc_website_test/2022/Event_name/Submissions/Rohit Singh-ropsingh@iu.edu",
                  file_path=abstract,
                  file_name=file_name,
                  mime_type=mime_type)

