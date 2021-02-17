from flask import Flask, render_template
import numpy as np
import os
import cv2
from keras.models import load_model
"""
Package      :version
-----------------------
pip          : 20.3.3
Flask        : 1.1.2
Keras        : 2.4.3
h5py         : 2.10.0
numpy        : 1.17.3
scipy        : 1.4.1
tensorflow   : 2.3.0
opencv-python: 4.1.0.25
=======================
environment  : Raspbian
Device       : Raspberry Pi4 modelB
"""

app = Flask(__name__)
#  学習モデルを読み込む
model_1 = load_model('./cnn_vol.2_model_G.h5')
model_2 = load_model('./TL.h5')


def detect_face(image):
    # opencvを使って顔抽出
    image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
    # 顔認識の実行
    face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=2, minSize=(64, 64))

    # 顔が１つ以上検出された時
    if len(face_list) > 0:
        #  学習した時と同じ大きさにリサイズする
        img = cv2.resize(image, (64, 64))
        img = np.expand_dims(img, axis=0)
        name = detect_who(img)
    # 顔が検出されなかった時
    else:
        name = "anonymous"
    return name


def detect_who(img):
    # 予測
    res = ""
    names = ""
    if bunki == 1:
        #  分類
        test = model_1.predict(img)
        '''
        names = ["Kannna_Hashimoto", "Ayami_Nakajou", "Hana_Sugisaki", "Masaki_Suda", "Hiroshi_Abe",
                 "Suzu_Hirose", "Minami_Hamabe", "Makkenyu_Arata", "Ryusei_Yokohama", "Masato_Sakai"
                 ]
        '''
        names = ["橋本環奈", "中条あやみ", "杉咲花", "菅田将暉", "阿部寛",
                 "広瀬すず", "浜辺美波", "新田真剣佑", "横浜流星", "堺雅人"]
    elif bunki == 2:
        #  分類
        test = model_2.predict(img)
        '''
        names = ["Katsuji Takasugi", "Yumi Takahashi", "Mai Okamoto", "Kou Habata", "Yoshiyuki Saitou",
                 "Naoto Uchiyama", "Rei Fueki", "Yu Uchiike", "Hitoshi Muratsubaki", "Kenichi Kurihara",
                 "Rumi Kobayashi", "Masakatsu Isobe", "Kanou", "Ai Suzuki", "Jyuniti Makita",
                 "Motohiro Shibata", "Mizue Tadokoro", "Miyuki Ushiama", "Tikako Shizuno", "Shinobu Hara",
                 "Mamiko Harasawa", "Shintarou Nakajima"]
        '''
        names = ["高杉勝治", "高橋由美", "岡本麻衣", "幅田耕", "斎藤義之", "内山直人", "笛木怜", "内池雄", "村椿仁", "栗原健一",
                 "小林留美", "五十部昌克", "狩野", "鈴木藍", "牧田純一", "柴田智宏", "田所瑞絵", "牛尼みゆき", "静野智香子", "原忍",
                 "原澤真実子", "中島慎太郎"]
    #  値が一番大きかった要素をname_numに格納
    name_num = np.argmax(test)
    #  bunkiに従い名前をresに格納
    for i, name in enumerate(names):
        if i == name_num:
            if bunki == 1:
                res = name
            elif bunki == 2:
                res = name + "先生"
            break
    return res


# 1page
@app.route("/")
@app.route("/1page_top.html")
def top():
    return render_template("1page_top.html")


# 2page
@app.route("/2page_main.html")
def main():
    return render_template("2page_main.html")


bunki = 0


# 3page(G)
@app.route("/load_g")
def load1():
    global bunki
    bunki = 1
    return render_template("3page_loding_G.html")


# 3page(S)
@app.route("/load_s")
def load2():
    global bunki
    bunki = 2
    return render_template("3page_loding_S.html")


# 4page
@app.route("/test_g")
@app.route("/test_s")
def test():
    image = cv2.imread("./test.jpeg")
    b, g, r = cv2.split(image)
    image = cv2.merge([r, g, b])
    whoImage = detect_face(image)
    os.remove('test.jpeg')
    return render_template("4page_result.html", human=whoImage)


if __name__ == "__main__":
    app.run(threaded=False)
