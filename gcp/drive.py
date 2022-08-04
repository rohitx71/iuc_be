from __future__ import print_function

import io

from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload, MediaIoBaseUpload

from gcp.init_gcp import init


def get_files(drive_service):
    # Call the Drive v3 API
    results = drive_service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
        return
    print('Files:')
    for item in items:
        print(u'{0} ({1})'.format(item['name'], item['id']))


def get_folder_id(drive_service, folder_name, parent_folder_id=None):
    page_token = None
    while True:
        query = "mimeType='application/vnd.google-apps.folder' and name='"+folder_name+"'"+" and trashed = false"
        if parent_folder_id:
            query+= "and parents in '"+parent_folder_id+"'"
        response = drive_service.files().list(q=query,
                                              spaces='drive',
                                              fields='nextPageToken, files(id, name)',
                                              pageToken=page_token).execute()
        for file in response.get('files', []):
            # Process change
            print('Found file: %s (%s)' % (file.get('name'), file.get('id')))
            return file.get('id')
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
        return None


def create_folder(drive_service):
    file_metadata = {
        'name': 'Invoices/Test/Tester',
        'mimeType': 'application/vnd.google-apps.folder'
    }
    file = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()
    print('Folder ID: %s' % file.get('id'))


def create_folder_in_folder(drive_service, folder_name, parent_folder_id):
    folder_id = parent_folder_id

    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    if folder_id:
        file_metadata['parents'] = folder_id

    file = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()

    print('Folder ID: %s' % file.get('id'))
    return file.get('id')


def iterate_folders_recursively(drive_service, folder):
    # folder = "iuc_website_test/2022/Event_name/Submissions/Rohit Singh-ropsingh@iu.edu"
    folder_list = folder.split("/")
    parent_id = None

    for current_folder in folder_list:
        current_parent_id = get_folder_id(drive_service, current_folder, parent_id)
        if not current_parent_id:
            current_parent_id = create_folder_in_folder(drive_service, current_folder, parent_id)
            print("folder created=" + current_folder)
            print("created in parent" + parent_id)
        parent_id = current_parent_id
    return parent_id


def upload_file(drive_service, file_path, file_name, mime_type, parent_id):
    file_metadata = {'name': file_name.lower(), "parents":[parent_id]}
    # media = MediaFileUpload(file_path)

    # with open(file_path, 'rb') as FID:
    #     file_path = FID.read()
    file_path.seek(0)
    media = MediaIoBaseUpload(io.BytesIO(file_path.read()), mimetype=mime_type)
    # pylint: disable=maybe-no-member
    file = drive_service.files().create(body=file_metadata, media_body=media,
                                  fields='id').execute()
    print(F'File ID: {file.get("id")}')
    return True


if __name__ == '__main__':
    try:
        sheets_service, drive_service = init()
        # iterate_folders_recursively("iuc_website_test/2022/Event_name/Submissions/Rohit Singh-ropsingh@iu.edu")
        file_path = "/Users/rohitsingh/Documents/Projects/IUC/FormSubmission/gcp/init_gcp.py"
        upload_file(drive_service, file_path, "init_gcp.py", "1KTsRW0VwuORoGvPCLuVOVUQ9aFMhQ9Lp")
        # get_folder_id(drive_service, "test")
        # create_folder_in_folder("test", "1KTsRW0VwuORoGvPCLuVOVUQ9aFMhQ9Lp")
        # create_folder(drive_service)
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'main(): An error occurred: {error}')


# test # 2022 # Event_name # Submissions # Rohit Singh - ropsingh@iu.edu #
