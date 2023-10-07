#!/usr/bin/python3

# Import necessary modules
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Create a compressed archive of the 'web_static' directory.

    This function generates a timestamped .tgz archive of the 'web_static'
    folder and stores it in a 'versions' directory.
    The archive is named using the current timestamp.

    Returns:
        str: The path to the created archive if successful, None otherwise.
    """

    # Get the current timestamp for archive naming
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Define source and target directories
    source_folder = "web_static"
    target_folder = "versions"

    # Create the "versions" folder if it doesn't exist
    if not os.path.exists(target_folder):
        local("mkdir -p {}".format(target_folder))

    # Define the name of the archive
    archive_name = "web_static_{}.tgz".format(timestamp)

    # Create the .tgz archive using 'tar'
    result = local("tar -cvzf {}/{} {}".
                   format(target_folder, archive_name, source_folder))

    # Check if the archive creation was successful
    if result.succeeded:
        archive_path = "{}/{}".format(target_folder, archive_name)
        archive_size = os.path.getsize(archive_path)
        print("web_static packed: {} -> {}Bytes".
              format(archive_path, archive_size))
        return archive_path
    else:
        return None


# Call the 'do_pack' function when the script is run
if __name__ == "__main__":
    do_pack()
