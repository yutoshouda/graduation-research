import os

"""
dataディレクトリから画像を読み込んで顔を切り取ってfaceディレクトリに保存.
"""
names = ['KannaHashimoto', 'AyamiNakajou', 'MinamiHamabe', 'MoneKamishiraishi', 'HanaSugisaki',
         'EikoKoike', 'SuzuHirose', 'NanaMori', 'TaouTsuchiya',
         'TomoyaNakamura', 'MasakiSuda', 'GouAyano', 'RyouYoshizawa', 'HiroshiAbe',
         'MakkenyuArata', 'RyuseiYokohama', 'MasatoSakai', 'TatsuyaFujiwara'
         ]
out_dir = "./train"
os.makedirs(out_dir, exist_ok=True)
for i in range(len(names)):
    os.mkdir(out_dir + "/" + names[i])
