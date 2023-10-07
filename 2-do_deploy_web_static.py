#!/usr/bin/python3

"""
Fabric script to deploy the web_static archive to web servers.
"""


from fabric.api import *
import os

env.user = 'ubuntu'
env.hosts = ['34.207.188.213', '52.86.123.235']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it.

    Args:
        archive_path (str): The path to the archive file on the local machine.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """

    # Check if the archive file exists on the local machine
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        archive_no_ext = os.path.splitext(archive_filename)[0]
        remote_tmp_path = "/tmp/{}".format(archive_filename)
        remote_release_path = "/data/web_static/releases/{}/".format(
            archive_no_ext)

        # Upload the archive to /tmp/ on the web servers
        put(archive_path, remote_tmp_path)

        # Create the release folder if it doesn't exist
        run("mkdir -p {}".format(remote_release_path))

        # Uncompress the archive to the release folder
        run("tar -xzf {} -C {}".format(remote_tmp_path, remote_release_path))

        # Delete the archive from the web server
        run("rm {}".format(remote_tmp_path))

        # Move the contents to the proper location
        run("mv {}web_static/* {}".format(
            remote_release_path, remote_release_path))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(remote_release_path))

        print("New version deployed!")
        return True

    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    archive_path = "versions/web_static_20231007203211.tgz"
    result = do_deploy(archive_path)
    if result:
        print("Deployment successful!")
    else:
        print("Deployment failed.")
