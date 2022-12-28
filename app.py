from flask import Flask, redirect, url_for, render_template, send_file, request
import pytube
from pytube.cli import on_progress

import os




app = Flask(__name__)

path = os.getcwd () + "./downloads/"

@app.route('/')
def index():
  return render_template('index.html')

# crea la carpeta "downloads" si no existe
if not os.path.exists('./downloads'):
  os.makedirs('./downloads')




@app.route('/download', methods=['POST'])
def download():
  if request.method == "POST":
    url = request.form["video_url"]
    yt = pytube.YouTube(url)
    titulo = yt.title
    titulo = titulo.replace("/", "")
    titulo = titulo.replace(":", "")
    titulo = titulo.replace(";", "")
    titulo = titulo.replace("|", "")
    audio = yt.streams.filter(only_audio=True)
    mejor_audio = yt.streams.get_by_itag(140)
    print(audio)
    mejor_audio.download(filename=path + titulo + ".mp3")
    return redirect(url_for('index'))

   



if __name__ == '__main__':
  # DEBUG is SET to TRUE. CHANGE FOR PROD
  app.run(debug=True)

