#!/bin/bash
# Script that displays the OPTIONS for request
curl -sI "$1" | grep "Allow" | awk -F': ' '{print $2}'
