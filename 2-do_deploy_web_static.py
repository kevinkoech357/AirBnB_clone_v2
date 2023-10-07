#!/usr/bin/python3

"""
Fabric script to deploy the web_static archive to web servers.
"""


from fabric.api import *
import os
import argparse


def do_deploy(archive_path, hosts):
    """
    Distribute and deploy a web_static archive to web servers.

    Args:
        archive_path (str): The path to the archive file on the local machine.
        hosts (list): List of hostnames or IP addresses to deploy to.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """

    # Check if the archive file exists on the local machine
    if not os.path.exists(archive_path):
        return False

    try:
        # Loop through each host
        for host in hosts:
            env.host_string = host

            # Upload the archive to /tmp/ on the web server
            remote_tmp_path = "/tmp/{}".format(os.path.basename(archive_path))
            put(archive_path, remote_tmp_path)

            # Create the release folder if it doesn't exist
            remote_release_path = "/data/web_static/releases/{}/".format(
                os.path.splitext(os.path.basename(archive_path))[0])
            run("mkdir -p {}".format(remote_release_path))

            # Uncompress the archive to the release folder
            run("tar -xzf {} -C {}".format(
                remote_tmp_path, remote_release_path))

            # Delete the archive from the web server
            run("rm {}".format(remote_tmp_path))

            # Use sudo to remove the existing images and styles directories
            sudo("rm -rf {}/images".format(remote_release_path))
            sudo("rm -rf {}/styles".format(remote_release_path))

            # Move the contents to the proper location
            sudo("mv {}/web_static/* {}".format(
                remote_release_path, remote_release_path))

            # Delete the old symbolic link /data/web_static/current
            run("rm -rf /data/web_static/current")

            # Create a new symbolic link to the deployed code
            run("ln -s {} /data/web_static/current".format(
                remote_release_path))

        print("Deployment successful!")
        return True

    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--identity", required=True,
                        help="SSH identity file path")
    parser.add_argument("-u", "--user", required=True, help="SSH username")
    parser.add_argument("archive_path", help="Path to the archive file")
    parser.add_argument("hosts", nargs='+', help="Hostnames or IP addresses")

    args = parser.parse_args()

    env.key_filename = args.identity
    env.user = args.user

    result = do_deploy(args.archive_path, args.hosts)
    if result:
        print("Deployment successful!")
    else:
        print("Deployment failed.")
