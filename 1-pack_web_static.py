#!/usr/bin/python3

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    # Current timestamp for archive naming
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Directory paths
    source_folder = "web_static"
    target_folder = "versions"
    
    # Create the "versions" folder if it doesn't exist
    if not os.path.exists(target_folder):
        local("mkdir -p {}".format(target_folder))
    
    # Define the archive name
    archive_name = "web_static_{}.tgz".format(timestamp)
    
    # Create the .tgz archive
    result = local("tar -cvzf {}/{} {}".format(target_folder, archive_name, source_folder))

    if result.succeeded:
        archive_path = "{}/{}".format(target_folder, archive_name)
        archive_size = os.path.getsize(archive_path)
        print("web_static packed: {} -> {}Bytes".format(archive_path, archive_size))
        return archive_path
    else:
        return None
