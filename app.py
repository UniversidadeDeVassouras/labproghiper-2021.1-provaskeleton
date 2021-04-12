from flask import Flask, render_template
from categoria import Categoria
from video import Video

app = Flask(__name__)

videos_culinaria = [Video(1, 'Como fazer strogonoff'), Video(2, 'Como fazer risotto?')]
videos_trailers = [Video(3, 'Batman vs Superman'), Video(4, 'Vingadores Ultimato')]
videos_anime = [Video(5, 'One Piece Temp 200'), Video(6, 'Naturo Temporada 400')]

categoria_list = []
categoria_list.append(Categoria(1, 'Culinária', videos_culinaria))
categoria_list.append(Categoria(2, 'Trailers', videos_trailers))
categoria_list.append(Categoria(3, 'Anime', videos_anime))

@app.route("/")
def home():
    return render_template("home.html", categoria_list = categoria_list)

@app.route("/video/<id>")
def videos(id):
    for categoria in categoria_list:
        for video in categoria.get_video_list():
            if str(video.get_id()) == id:
                return render_template("video.html", video = video)
    return render_template("home.html", categoria_list = categoria_list)
