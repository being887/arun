from flask import Flask, render_template, redirect, url_for, request, send_file
from pytube import YouTube



app = Flask(__name__)
print("hello1")
@app.route("/")
def index():
    print("hello2")
    return render_template('index.html')

@app.route("/download", methods=["POST"])
def download():
    url = request.form["url"]
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video_filename = video.default_filename
    video.download()
    return "video is downloaded successfully"
   

if __name__ == "__main__":
   app.run(host="0.0.0.0",port=5000)
