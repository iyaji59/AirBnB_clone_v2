#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
# creates folders, /data/, /data/web_static/. /data/web_static/releases/
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
web="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo "$web" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default
service nginx restart
