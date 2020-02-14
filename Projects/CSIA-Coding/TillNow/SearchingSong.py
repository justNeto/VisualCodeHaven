from __future__ import unicode_literals
import speech_recognition as sr
import os
import numpy as np
import requests
import time
import unidecode
import json
import random
import urllib.request
import urllib.parse
import re
import urllib.request
import urllib.parse
import youtube_dl
import librosa

def listen_song_name():
    r = sr.Recognize()
    with sr.Microphone() as source:
        print('Speak')
        audio = r.listen(source)
        try:
            song_name = r.listen(source)
            return song_name
            return True
            break
        except:
            print("Sorry, could you please repeat that")
            break
        except:
            print("There is a problem")
            break
    
   
def process_audio(y, sr=44100):         #Extract characteristics
    rmse = librosa.feature.rmse(y=y)
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    to_append = f'{np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
    for e in mfcc:
        to_append += f' {np.mean(e)}'
    song = np.array([float(x) for x in to_append.split()])
    return np.reshape(song, (1,26))
    
if listen_song_name() is True:
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
y, sr = librosa.load('')
song = process_audio(y, sr)
