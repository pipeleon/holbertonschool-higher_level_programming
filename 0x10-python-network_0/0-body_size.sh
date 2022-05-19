#!/bin/bash
# Script that displays the size of the body of the response
curl -sI 0.0.0.0:5000 | grep 'Content-Length' | awk '{print $2}'
