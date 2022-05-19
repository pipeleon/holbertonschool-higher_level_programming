#!/bin/bash
# Script that displays the result of sending a header specific
curl -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
