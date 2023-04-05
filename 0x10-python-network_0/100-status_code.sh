#!/bin/bash
#send a jason post request to a given url with a JSON file
curl -o /dev/null -s -w "%{http_code}\n" "$1"
