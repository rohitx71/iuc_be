import json

from gcp.main import gdrive_helper


def parse(theme, affiliation, first_name, last_name, email, phone_number, university, street_address, city, state,
          country, zip_code, secondary_authors, abstract, file_name, mime_type):

    # create folders in drive

    # upload pdf to drive

    # vimeo

    is_abstract_uploaded = True if abstract else "Abstract not uploaded"
    final_data = [is_abstract_uploaded, theme, affiliation, first_name, last_name, email, phone_number, university, street_address, city,
                  state, country, zip_code]

    # deserialize secondary_authors
    secondary_authors = json.loads(secondary_authors)
    if secondary_authors:
        print(secondary_authors)
        for i in secondary_authors:
         #   print(i)
            final_data.append(i['first_name'])
            final_data.append(i['last_name'])
            final_data.append(i['affiliation'])

    final_name = first_name + " " + last_name + "-" + email

    # append values to sheet
    gdrive_helper(sheets_data=final_data,
                  folder="my_website/2022/PTS_Conference/Submissions/" + final_name,
                  file_path=abstract,
                  file_name=final_name + "/" + file_name,
                  mime_type=mime_type)

