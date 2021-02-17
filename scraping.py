import requests
import random
import shutil
import bs4
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context

path_url = "C:/Users/spide/PycharmProjects/Deep_Learning.2.0/data/"

names = ['KannaHashimoto', 'AyamiNakajou', 'MinamiHamabe', 'MoneKamishiraishi', 'HanaSugisaki',
         'EikoKoike', 'SuzuHirose', 'NanaMori', 'TaouTsuchiya',
         'TomoyaNakamura', 'MasakiSuda', 'GouAyano', 'RyouYoshizawa', 'HiroshiAbe',
         'MakkenyuArata', 'RyuseiYokohama', 'MasatoSakai', 'TatsuyaFujiwara'
         ]
search_names = ['橋本環奈', '中条あやみ', '浜辺美波', '上白石萌音',
                '小池栄子', '今田美桜', '広瀬すず', '森七菜', '土屋太鳳',
                '中村倫也', '菅田将暉', '綾野剛', '吉沢亮', '阿部寛',
                '新田真剣佑', '横浜流星', '堺雅人', '藤原竜也', 'ムロツヨシ'
                ]


def image(data):
    Res = requests.get("https://www.google.com/search?hl=jp&q=" + data + "&btnG=Google+Search&tbs=0&safe=off&tbm=isch")
    Html = Res.text
    Soup = bs4.BeautifulSoup(Html, 'lxml')
    links = Soup.find_all("img")
    link = random.choice(links).get("src")
    return link


def download_img(url, file_name, i):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path_url + file_name + "/" + file_name + "_{0:05d}".format(i + 1) + ".jpg", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


num = input("検索回数:")

for j, s_name in enumerate(search_names):
    for i in range(int(num)):
        link = image(s_name)
        if link.endswith(".gif"):
            continue
        download_img(link, names[j], i)
        time.sleep(1)
    time.sleep(1)
print("Completed!")
