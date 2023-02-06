from flask import Flask, render_template, redirect, url_for, request, send_file
from pytube import YouTube
import requests, os
import json
os.environ['FLASK_ENV'] = 'production'

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/download", methods=["POST"])
def download():
    url = request.form["url"]
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video_filename = video.default_filename
    video.download()
   

if __name__ == "__main__":
   app.run()
