import time
import requests


# part1:トップニュースのIDを50件取得してリスト化
def Top_id_List():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    response_top_id = requests.get(url)  # トップニュースのID取得
    top_id_js = response_top_id.json()  # トップニュースのIDをパース

    top_id_l = []  # 空リスト、トップニュースのIDが入る
    for n in range(50):  # 50件のIDを空リストへ
        top_id_l.append(top_id_js[n])
        time.sleep(0.5)  # ここで0.5秒止まる
    return top_id_l


top_id_l = Top_id_List()


# part2:トップニュース50件のタイトルとURLを辞書で出力
def main():
    for n in range(len(top_id_l)):
        story_dic = {}  # 空辞書
        url = f"https://hacker-news.firebaseio.com/v0/item/{top_id_l[n]}.json?print=pretty"
        response_topstories = requests.get(url)  # トップニュースを取得
        topstory = response_topstories.json()  # トップニュースをパース

        story_dic.setdefault("title:", f"{topstory['title']}")
        if "url" in topstory:
            story_dic.setdefault("link:", f"{topstory['url']}")
        else:
            pass
        time.sleep(1)  # ここで1秒止まる
        print(story_dic)


if __name__ == "__main__":
    main()


# printのエラーは直せない？
