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

name_of_song = input("Give me the name of the song")

query_string = urllib.parse.urlencode({"search_query" : name_of_song})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
url = "http://www.youtube.com/watch?v=" + search_results[0]
    
ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
