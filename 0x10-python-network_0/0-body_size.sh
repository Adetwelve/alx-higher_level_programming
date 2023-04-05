#!/bin/bash
#using curl displays the size of the body of the url
curl -s "$1" | wc -m
