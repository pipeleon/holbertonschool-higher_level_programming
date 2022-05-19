#!/bin/bash
# Script that displays the result of sending a header specific
curl -s -X POST "$1" -H 'Content-Type: application/json' -d @"$2"
