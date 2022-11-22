#!/bin/sh

# This script is used to run the proxy server.
set -e

envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
nginx -g "daemon off;"

