import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_player_stats():
    url = "https://www.baseball-reference.com/players/o/ohtansh01.shtml"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # 打撃成績のテーブルを取得
    table = soup.find("table", {"id": "batting_standard"})
    df = pd.read_html(str(table))[0]

    # 必要なデータ処理を行う
    df = df.dropna(how="all")  # 不要な行を削除
    return df.to_dict()  # データを辞書形式で返す


def get_news():
    # Yahoo!ニュースの検索URL（大谷翔平で検索）
    url = "https://news.yahoo.co.jp/search?p=大谷翔平&ei=UTF-8"

    # ページの内容を取得
    response = requests.get(url)
    response.raise_for_status()

    # BeautifulSoupでHTMLを解析
    soup = BeautifulSoup(response.content, "html.parser")

    # ニュースのタイトルとリンクを取得
    news_list = []
    articles = soup.find_all("a", class_="newsFeed_item_link")

    for article in articles:
        title = article.get_text(strip=True)
        link = article["href"]
        news_list.append({"title": title, "link": link})

    return news_list
