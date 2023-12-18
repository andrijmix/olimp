import shutil
from ftplib import FTP
import os

from settings import ftp_host, ftp_username, ftp_password, local_folder_path, ftp_folder_path


def download_folder_ftp(ftp_host, ftp_username, ftp_password, ftp_folder_path, local_folder_path):
    print("Downloading folder from FTP server...")
    # Remove all contents from the local folder if it exists
    # if os.path.exists(local_folder_path):
    #     shutil.rmtree(local_folder_path)
    try:
        # Connect to the FTP server
        ftp = FTP(ftp_host)
        ftp.login(user=ftp_username, passwd=ftp_password)

        # Move to the specified directory on the FTP server
        ftp.cwd(ftp_folder_path)

        # Create the local folder if it doesn't exist
        if not os.path.exists(local_folder_path):
            os.makedirs(local_folder_path)

        # Function to download files and subdirectories
        def download_files(ftp, local_path):
            # Get the list of files and directories on the server
            items = ftp.nlst()

            for item in items:
                local_item = os.path.join(local_path, item)
                if ftp.nlst(item) != [item]:  # Check if 'item' is a directory
                    os.makedirs(local_item, exist_ok=True)
                    ftp.cwd(item)
                    download_files(ftp, local_item)  # Recursive call to download contents of the directory
                    ftp.cwd('..')
                else:
                    with open(local_item, 'wb') as f:
                        ftp.retrbinary('RETR ' + item, f.write)

        # Download files and subdirectories
        download_files(ftp, local_folder_path)

        # Close the connection to the FTP server
        ftp.quit()
        print("Folder successfully downloaded from FTP server")

    except Exception as e:
        print(f"Error: {e}")


# download_folder_ftp(ftp_host, ftp_username, ftp_password,ftp_folder_path,local_folder_path)
