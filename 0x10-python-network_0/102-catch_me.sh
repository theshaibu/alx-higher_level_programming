#!/bin/bash
# Send a request to 0.0.0.0:5000/catch_me to make the server respond with "You got me!"

curl -sX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin:HolbertonSchool"

