from __future__ import division
import sys, json;

# Receive the data passed from runApp.js
data = json.load(sys.stdin)

# Parse the data for 'user'
youtubeData = data[0]['youtube']
channelStatistics = youtubeData[0]['channelStatistics']
items = channelStatistics['items'][0]
statistics = items['statistics']

# Parse statistics data
viewCount = statistics['viewCount']
commentCount = statistics['commentCount']
subscriberCount = statistics['subscriberCount']
videoCount = statistics['videoCount']

# Format into html (with bootstrap)
html = '<div class="container" style="padding-top: 20px">View Count: ' + str(viewCount) + '<br>comment Count : ' + str(commentCount) + '<br>Subscriber Count: ' + str(subscriberCount) + '<br>Video Count: ' + str(videoCount) + '</div>'

# Output
print(json.dumps({'html': html}))
