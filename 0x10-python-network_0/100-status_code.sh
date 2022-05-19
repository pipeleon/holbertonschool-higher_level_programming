#!/bin/bash
# Script that displays the result of sending a header specific
curl --write-out '%{http_code}' --silent --output /dev/null -sL "$1"
