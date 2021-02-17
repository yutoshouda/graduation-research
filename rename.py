import glob
import os

names = ['KannaHashimoto', 'AyamiNakajou', 'MinamiHamabe', 'MoneKamishiraishi', 'HanaSugisaki',
         'EikoKoike', 'SuzuHirose', 'NanaMori', 'TaouTsuchiya',
         'TomoyaNakamura', 'MasakiSuda', 'GouAyano', 'RyouYoshizawa', 'HiroshiAbe',
         'MakkenyuArata', 'RyuseiYokohama', 'MasatoSakai', 'TatsuyaFujiwara'
         ]

# 画像の名前を変更するディレクトリ
for name in names:
    img_dir = "./train/" + name + "/"
    images_list = glob.glob(img_dir + "*")

    for i, image in enumerate(images_list):
        dst = img_dir + name + "_{0:05d}".format(i + 1) + ".jpg"
        os.rename(image, dst)
        print("rename:" + dst)
