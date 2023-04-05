#!/bin/bash
#using curl displays the size of the body of the
curl -sI '$1' | grep Content-Length | cut -d " " -f 2
