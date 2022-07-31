from gcp.init_gcp import init
from gcp.drive import iterate_folders_recursively, upload_file
from gcp.sheets import append_values


def gdrive_helper(sheets_data, folder, file_path, file_name, mime_type):
    sheets_service, drive_service = init()
    # get_files(drive_service)
    if file_path:
        parent_id = iterate_folders_recursively(drive_service, folder)
        upload_file(drive_service, file_path, file_name, mime_type, parent_id)
    append_values(sheets_service, sheets_data)

    # get_folder_id(drive_service, "Yt")
    # create_folder(drive_service)

#
if __name__ == "__main__":
    gdrive_helper()