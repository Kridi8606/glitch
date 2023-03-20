import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """<div style="width: 560px; margin-left: auto; margin-right: auto; text-align: center;"><h1>Somewhere in Nevada</h1>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/-KxAyqBrfVc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>"""


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port)