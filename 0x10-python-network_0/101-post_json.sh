#!/bin/bash
# POST a JSON request to a given URL with a given JSON file.
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
