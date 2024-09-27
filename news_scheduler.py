import schedule
import time
from scraper import get_news  # ニュース取得関数をインポート


# ニュース取得と処理を行う関数
def fetch_news():
    news = get_news()
    print("最新ニュースを取得しました:")
    for item in news:
        print(f"タイトル: {item['title']}\nリンク: {item['link']}\n")


# スケジュール設定: 1時間ごとにニュースを取得
schedule.every(1).hours.do(fetch_news)

# 無限ループでスケジュールされたタスクを実行
while True:
    schedule.run_pending()
    time.sleep(3600)  # 3600秒ごとにチェック
