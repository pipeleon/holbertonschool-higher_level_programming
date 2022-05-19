#!/bin/bash
# Script that displays the body of the response
response=$(curl --write-out '%{http_code}' --silent --output /dev/null -L "$1")
OK="200"
if [[ "$response" -eq "$OK" ]]; then
    curl -L "$1"
fi
