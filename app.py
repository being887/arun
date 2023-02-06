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
    app.logger.debug(f'Downloaded file: {video_filename}')
    try:
        return send_file(video_filename, as_attachment=True)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=9000)
