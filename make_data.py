import os, glob, random
import cv2
from PIL import Image
import numpy as np

# 画像フォルダが存在するディレクトリ
image_dir = "./face/"
# カテゴリ毎に分類(フォルダ名)
category = ['KannaHashimoto', 'AyamiNakajou', 'MinamiHamabe', 'MoneKamishiraishi', 'HanaSugisaki',
            'EikoKoike', 'SuzuHirose', 'NanaMori', 'TaouTsuchiya',
            'TomoyaNakamura', 'MasakiSuda', 'GouAyano', 'RyouYoshizawa', 'HiroshiAbe',
            'MakkenyuArata', 'RyuseiYokohama', 'MasatoSakai', 'TatsuyaFujiwara'
            ]
# 出力するnpyファイル名
out_npy = "act_rgb.npy"
# 画像のサイズ(縦横60px)
image_size = 60

# 画像を格納する配列
X_train = []
X_val = []
# ラベルデータを格納する配列
Y_train = []
Y_val = []


# OpenCVの画像データをPILに変換
def convert_cv2pil(image_cv):
    image_pil = Image.fromarray(image_cv)
    image_pil = image_pil.convert('RGB')
    image_pil = np.asarray(image_pil)

    return image_pil


# 学習用の配列に追加
def append_train(image, index):
    image = convert_cv2pil(image)
    global X_train
    global Y_train
    data = np.asarray(image)
    X_train.append(image)
    Y_train.append(index)


# 確認用の配列に追加
def append_val(image, index):
    image = convert_cv2pil(image)
    global X_val
    global Y_val
    data = np.asarray(image)
    X_val.append(image)
    Y_val.append(index)


# カテゴリのループ
for index, category_name in enumerate(category):
    # 画像の読み込み
    images_dir = image_dir + category_name
    files = glob.glob(images_dir + "/*.jpg")
    # 画像のシャッフル
    random.shuffle(files)
    # 10%の画像をテストデータに
    test_num = int(len(files) * 0.1)

    # 画像の取り出し
    for i, file in enumerate(files):
        # 画像の読み込み
        image = cv2.imread(file)
        print("open_img:{}".format(file))
        # リサイズ
        image = cv2.resize(image, (image_size, image_size))

        # 読み込み枚数がtest_num以下の場合はテストに以降は訓練に格納
        if i < test_num:
            append_val(image, index)
        else:
            # 訓練データの水増し
            for i in range(-5, 6, 5):
                # 回転
                center = int(image.shape[1] / 2)
                rotate = cv2.getRotationMatrix2D((center, center), i, 1)
                img = cv2.warpAffine(image, rotate, (image_size, image_size), flags=cv2.INTER_CUBIC)
                append_train(img, index)

                # 反転
                img = cv2.flip(img, 1)
                append_train(img, index)

                # ぼかし
                img_b = cv2.GaussianBlur(img, (5, 5), 0)
                append_train(img_b, index)

                # 闘値
                img_t = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                img_t = cv2.threshold(img_t, 100, 255, cv2.THRESH_TOZERO)[1]
                append_train(img_t, index)

# numpyの配列形式に変換
X_train = np.array(X_train)
X_val = np.array(X_val)
Y_train = np.array(Y_train)
Y_val = np.array(Y_val)

# 配列に変換した画像を保存
data = (X_train, X_val, Y_train, Y_val)
np.save("./" + out_npy, data)
print("Success:create ./" + out_npy)
