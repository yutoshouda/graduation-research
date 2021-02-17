from flask import Flask, render_template
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
from keras.models import load_model
import time

app = Flask(__name__)

model = load_model('./cnn_vol.2_model_G.h5')


def detect_face(image):
    # opencvを使って顔抽出
    image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
    # 顔認識の実行
    face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=2, minSize=(64, 64))

    # 顔が１つ以上検出された時
    if len(face_list) > 0:
        for rect in face_list:
            x, y, width, height = rect
            cv2.rectangle(image, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), (255, 0, 0), thickness=3)
            img = image[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]]
            if image.shape[0] < 64:
                print("too small")
                continue
            img = cv2.resize(image, (64, 64))
            img = np.expand_dims(img, axis=0)
            name = detect_who(img)
            # cv2.putText(image, name, (x, y + height + 20), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)
    # 顔が検出されなかった時
    else:
        name = "anonymouse"
    return name


def detect_who(img):
    # 予測
    name = ""
    print("fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")
    nameNumLabel = np.argmax(model.predict(img))

    if nameNumLabel == 0:
        name = "Kannna Hashimoto"
    elif nameNumLabel == 1:
        name = "Ayami Nakajou"
    elif nameNumLabel == 2:
        name = "Hana Sugisaki"
    elif nameNumLabel == 3:
        name = "Masaki Suda"
    elif nameNumLabel == 4:
        name = "Hiroshi Abe"
    elif nameNumLabel == 5:
        name = "Suzu Hirose"
    elif nameNumLabel == 6:
        name = "Minami Hmabe"
    elif nameNumLabel == 7:
        name = "Makkenyu Arata"
    elif nameNumLabel == 8:
        name = "Ryusei Yokohama"
    elif nameNumLabel == 9:
        name = "Masato Sakai"
    return name


# 1page
@app.route("/")
def top():
    return render_template("1page_top.html")


# 2page
@app.route("/2page_main.html")
def main():
    return render_template("2page_main.html")


# 3page(G)
@app.route("/load_g")
def load1():
    return render_template("3page_loding_G.html")


# 3page(S)
@app.route("/load_s")
def load2():
    return render_template("3page_loding_S.html")


# 4page
@app.route("/test_g")
def test():
    time.sleep(0.5)
    image = cv2.imread("./test.jpeg")
    b, g, r = cv2.split(image)
    image = cv2.merge([r, g, b])
    whoImage = detect_face(image)
    percent = 50
    os.remove('test.jpeg')
    return render_template("4page_result.html", human=whoImage, percent=percent)
    # return render_template("4page_result.html")


@app.route("/test_s")
def test2():
    a = 25
    b = 40
    percent = a + b

    human = "NaotoUtiyama"

    return render_template("4page_result.html", human=human, percent=percent)


@app.route("/1page_top.html")
def do():
    return render_template("1page_top.html")


if __name__ == "__main__":
    X = np.zeros((10, 100))
    model.predict_proba(X, batch_size=32)
    app.run()
