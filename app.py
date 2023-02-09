from flask import Flask, render_template, redirect, url_for, request, send_file
from pytube import YouTube



app = Flask(__name__)
print("hello1")
@app.route("/")
def index():
    print("hello2")
    return render_template("../templates/index.html")

@app.route("/download", methods=["POST"])
def download():
    try:
        url = request.form["url"]
        yt = YouTube(url)
        
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        print("hello3")
        video_filename = video.default_filename
        video.download()
        return send_file(video_filename, as_attachment=True)
    except Exception as e:
        return "An error occurred while downloading the video: " + str(e)


   

if __name__ == "__main__":
   app.run(host="0.0.0.0",port=4000)
