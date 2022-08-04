import json

from gcp.main import gdrive_helper
from aws.send_dynamic_email_sendgrid import send_dynamic_email


def parse(theme, affiliation, first_name, last_name, email, phone_number, university, street_address, city, state,
          country, zip_code, secondary_authors, abstract, file_name, mime_type, title):

    # create folders in drive

    # upload pdf to drive

    # vimeo

    import datetime

    # using now() to get current time
    current_time = str(datetime.datetime.now())

    is_abstract_uploaded = True if abstract else "Abstract not uploaded"
    final_data = [0, current_time, is_abstract_uploaded, theme, affiliation, first_name, last_name, email, phone_number,
                  university, street_address, city, state, country, zip_code]

    # deserialize secondary_authors
    secondary_authors = json.loads(secondary_authors)
    email_secondary_authors = ""
    if secondary_authors:
        print(secondary_authors)
        for i in secondary_authors:
         #   print(i)
            if email_secondary_authors:
                email_secondary_authors += ", "
            final_data.append(i['first_name'])
            final_data.append(i['last_name'])
            final_data.append(i['affiliation'])
            email_secondary_authors += i['first_name'] + " " + i['last_name']

    final_name = first_name + " " + last_name + "-" + email

    # append values to sheet
    id = gdrive_helper(sheets_data=final_data,
                  folder="my_website/2022/PTS_Conference/Submissions/" + final_name,
                  file_path=abstract,
                  file_name=final_name + "/" + file_name,
                  mime_type=mime_type)

    from time import localtime, strftime
    datetime = strftime("%a, %d %b", localtime())
    send_dynamic_email(email, datetime, id, title, theme, first_name + " " + last_name, phone_number,
                       secondary_authors=email_secondary_authors)

