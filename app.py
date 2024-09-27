import os
from flask import Flask, render_template
from scraper import get_player_stats, get_news  # ニュース取得関数をインポート

app = Flask(__name__)


@app.route("/")
def index():
    stats = get_player_stats()  # 選手の成績を取得
    news = get_news()  # 最新のニュースを取得
    return render_template("index.html", stats=stats, news=news)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)
