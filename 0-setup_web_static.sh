#!/usr/bin/env bash
# This script sets up my web servers
# before deployment of static

# Update packages and install nginx
sudo apt update -y
sudo apt install nginx -y

# Operations to perform
# Setting up directories if they dont exist
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Setting up index.html for testing
echo "<html>
  <head>
  </head>
  <body>
    Kevin Koech
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create or update the symbolic link
if [ -L /data/web_static/current ]
then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data

# Add Nginx configuration for serving static files
echo "server {
    listen 80 default_server; # Listen on port 80 for incoming requests
    listen [::]:80 default_server; # Listen on IPv6 address

    root /var/www/html; # Set the root directory for the server

    index index.html index.htm index.nginx-debian.html; # Specify default index files

    server_name _; # Catch-all server name

    add_header X-Served-By 246664-web-01; # Add a custom header to responses
    error_page 404 /custom_404.html; # Define a custom 404 error page
    rewrite ^/redirect_me https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent; # Redirect a specific URL

    # Serve static files from /data/web_static/current/ when the URL path starts with /hbnb_static
    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html; # Specify the default index file
    }

    location / {
        # First attempt to serve request as file, then
        # as directory, then fall back to displaying a 404.
        try_files \$uri \$uri/ =404;
    }
}" | sudo tee /etc/nginx/sites-available/default

# Restart nginx server
sudo service nginx restart
