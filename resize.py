import os
import cv2
import glob


names = ['KannaHashimoto', 'AyamiNakajou', 'MinamiHamabe', 'MoneKamishiraishi', 'HanaSugisaki',
         'EikoKoike', 'SuzuHirose', 'NanaMori', 'TaouTsuchiya',
         'TomoyaNakamura', 'MasakiSuda', 'GouAyano', 'RyouYoshizawa', 'HiroshiAbe',
         'MakkenyuArata', 'RyuseiYokohama', 'MasatoSakai', 'TatsuyaFujiwara'
         ]

for name in names:
    in_dir = "./train/" + name + "/*"
    out_dir = "./train/" + name + "/*"
    in_jpg = glob.glob(in_dir)
    img_file_name_list = os.listdir("./train/" + name + "/")
    for i in range(len(in_jpg)):
        # print(str(in_jpg[i]))
        img = cv2.imread(str(in_jpg[i]))
        img_rot = cv2.resize(img, (64, 64))
        fileName = os.path.join(out_dir, "_{0:05d}".format(i + 1) + ".jpg")
        cv2.imwrite(str(fileName), img_rot)
    print(name + "_completed!")
