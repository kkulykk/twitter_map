"""
Main Flask module 
"""
from flask import Flask, render_template, request, redirect
import twitter_api
import main

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST", "GET"])
def gen_map():
    if request.method == "POST":
        nickname = str(request.form["nickname"])
        token = str(request.form["token"])
        try:
            main.build_map(main.get_coordinates(main.parse_json(
                twitter_api.get_followers(nickname, token))))
        except:
            return redirect('/error')
        return render_template("map.html")


@app.route('/error')
def error():
    return render_template("error.html")


if __name__ == '__main__':
    app.run()
