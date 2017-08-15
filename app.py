from __future__ import division
import sys, json;

# Receive the data passed from runApp.js
data = json.load(sys.stdin)

# Parse the data for 'user'
fitbitData = data[0]['fitbit']
profileData = fitbitData[0]['profile']
userData = profileData[0]['user']

# Parse Fitbit data
displayName = userData['displayName']
weight = round(userData['weight'] * 2.2, 2)
height = round(userData['height'] / 2.54, 2)

greeting = displayName

# Format into html (with bootstrap)
html = '<div class="container">' + greeting + '<br>Weight: ' + str(weight) + '<br>Height: ' + str(height) + '</div>'

# Output
print(json.dumps({'html': html}))
