from __future__ import unicode_literals
import os
import requests
import unidecode
import json
import random
import urllib.request
import urllib.parse
import re
import urllib.request
import urllib.parse
import youtube_dl

ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
}

# Declares the name of song
song = input("\n Give me the name of the song")
print("You will download", song)

if song[:4] == "http":
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([song])
else:
	query_string = urllib.parse.urlencode({"search_query" : song})
	html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
	url = "http://www.youtube.com/watch?v=" + search_results[0]
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])