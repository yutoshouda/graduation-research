import numpy as np
import matplotlib.pyplot as plt
import cv2
from keras.models import load_model
import sys


def detect_face(image):
    print(image.shape)
    # opencvを使って顔抽出
    image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier("./cascade_file/haarcascade_frontalface_alt.xml")
    # 顔認識の実行
    face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=2, minSize=(64, 64))
    # 顔が１つ以上検出された時
    if len(face_list) > 0:
        for rect in face_list:
            x, y, width, height = rect
            # 下２行は画像に描画する処理
            cv2.rectangle(image, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), (255, 0, 0), thickness=3)
            img = image[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]]
            if image.shape[0] < 64:
                print("too small")
                continue
            # リサイズ（学習した時と同じサイズにしないとエラーになる）
            img = cv2.resize(image, (64, 64))
            # １次元にする
            img = np.expand_dims(img, axis=0)
            name = detect_who(img)
            # 画像に結果を出力
            cv2.putText(image, name, (x, y + height + 20), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)
    # 顔が検出されなかった時
    else:
        print("no face")
    return image


def detect_who(img):
    # 予測
    names = ['KannaHashimoto', 'AyamiNakajou', 'HanaSugisaki', 'MinamiHamabe', 'SuzuHirose,',
             'MasakiSuda', 'HiroshiAbe', 'MakkenyuArata', 'RyuseiYokohama', 'MasatoSakai'
             ]
    res = ""
    print(model.predict(img))
    nameNumLabel = np.argmax(model.predict(img))
    for name, i in enumerate(names):
        if nameNumLabel == i:
            res = name

    return res


if __name__ == '__main__':
    # モデルをロード
    model = load_model('./my_model.h5')
    # テスト画像を読み込み
    image = cv2.imread("./test.jpg")
    b, g, r = cv2.split(image)
    image = cv2.merge([r, g, b])
    whoImage = detect_face(image)

    plt.imshow(whoImage)
    plt.show()
