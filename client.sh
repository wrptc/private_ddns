#!/bin/bash
HOST="HOST"
SERVER="http://0.0.0.0:5000/hosts"
IP=$(curl -s api.ipify.org)
curl -d "dest=$IP&host=$HOST" $SERVER
