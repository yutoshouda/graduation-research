import shutil
import random
import glob
import os

names = ['KannaHashimoto', 'AyamiNakajou', 'MinamiHamabe', 'MoneKamishiraishi', 'HanaSugisaki',
         'EikoKoike', 'SuzuHirose', 'NanaMori', 'TaouTsuchiya',
         'TomoyaNakamura', 'MasakiSuda', 'GouAyano', 'RyouYoshizawa', 'HiroshiAbe',
         'MakkenyuArata', 'RyuseiYokohama', 'MasatoSakai', 'TatsuyaFujiwara'
         ]

for name in names:
    in_dir = "./face/" + name + "/*"
    in_jpg = glob.glob(in_dir)
    img_file_name_list = os.listdir("./face/" + name + "/")
    # img_file_name_listをシャッフル、そのうち2割をtest_imageディテクトリに入れる
    random.shuffle(in_jpg)
    for t in range(len(in_jpg) // 5):
        shutil.move(str(in_jpg[t]), "./test/" + name)
