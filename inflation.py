import os
import cv2
import glob
from scipy import ndimage

"""
faceディレクトリから画像を読み込んで回転、ぼかし、閾値処理をしてtrainディレクトリに保存する.
"""
names = ['KannaHashimoto', 'AyamiNakajou', 'MinamiHamabe', 'MoneKamishiraishi', 'HanaSugisaki',
         'EikoKoike', 'SuzuHirose', 'NanaMori', 'TaouTsuchiya',
         'TomoyaNakamura', 'MasakiSuda', 'GouAyano', 'RyouYoshizawa', 'HiroshiAbe',
         'MakkenyuArata', 'RyuseiYokohama', 'MasatoSakai', 'TatsuyaFujiwara'
         ]

for name in names:
    in_dir = "./face/" + name + "/*"
    out_dir = "./train/" + name
    in_jpg = glob.glob(in_dir)
    img_file_name_list = os.listdir("./face/" + name + "/")
    for i in range(len(in_jpg)):
        # print(str(in_jpg[i]))
        img = cv2.imread(str(in_jpg[i]))
        # 回転
        for ang in [-5, 0, 5]:
            img_rot = ndimage.rotate(img, ang)
            img_rot = cv2.resize(img_rot, (256, 256))
            fileName = os.path.join(out_dir, str(i) + "_" + str(ang) + ".jpg")
            cv2.imwrite(str(fileName), img_rot)
            # 閾値
            img_thr = cv2.threshold(img_rot, 100, 255, cv2.THRESH_TOZERO)[1]
            fileName = os.path.join(out_dir, str(i) + "_" + str(ang) + "thr.jpg")
            cv2.imwrite(str(fileName), img_thr)
            # ぼかし
            img_filter = cv2.GaussianBlur(img_rot, (5, 5), 0)
            fileName = os.path.join(out_dir, str(i) + "_" + str(ang) + "filter.jpg")
            cv2.imwrite(str(fileName), img_filter)
            # 反転
            img_turning = cv2.flip(img_rot, 1)
            fileName = os.path.join(out_dir, str(i) + "_" + str(ang) + "turning.jpg")
            cv2.imwrite(str(fileName), img_turning)
    print(name + "_completed!")
