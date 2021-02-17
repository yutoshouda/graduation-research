# 普通に学習２

import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
from keras.utils import plot_model
import pydot

# npyファイルの読み込み
in_npy = "act_rgb.npy"
# 出力するモデル名を指定
out_model = "cnn_vol.2_model.h5"

# CNN設定
CATEGORY_NUM = 35
BATCH_SIZE = 128
EPOCHS = 100
LEARNING_RATE = 0.0001


def main():
    # gen_data.pyで生成したRGB形式の画像データを読み込む
    X_train, X_val, Y_train, Y_val = np.load("./" + in_npy, allow_pickle=True)
    # 正規化を行う(最大値:256で割って0〜1に収束)
    X_train = X_train.astype("float") / 256
    X_val = X_val.astype("float") / 256
    # ラベルをベクトルに変換
    Y_train = np_utils.to_categorical(Y_train, CATEGORY_NUM)
    Y_val = np_utils.to_categorical(Y_val, CATEGORY_NUM)

    # 学習の実行
    model = model_train(X_train, Y_train, X_val, Y_val)


def model_train(X, Y, Xv, Yv):
    # モデルの定義
    model = Sequential()

    model.add(Conv2D(32, (3, 3), padding='same', input_shape=X.shape[1:]))
    model.add(Activation('relu'))

    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))

    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())

    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(CATEGORY_NUM))
    model.add(Activation('softmax'))

    # モデルの可視化
    plot_model(model, to_file='model_' + str(EPOCHS) + '.png')

    # 最適化処理
    opt = keras.optimizers.rmsprop(lr=LEARNING_RATE, decay=1e-6)

    # モデル最適化の宣言
    model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

    # 学習
    result = model.fit(X, Y, batch_size=BATCH_SIZE, epochs=EPOCHS, validation_data=(Xv, Yv))

    # モデルデータの保存
    model.save('./' + out_model)
    print("Success:create ./" + out_model)

    # グラフ表示
    plt.plot(range(1, EPOCHS + 1), result.history['accuracy'], label="train-acc")
    plt.plot(range(1, EPOCHS + 1), result.history['loss'], label="train-loss")
    plt.plot(range(1, EPOCHS + 1), result.history['val_accuracy'], label="val-acc")
    plt.plot(range(1, EPOCHS + 1), result.history['val_loss'], label="val-loss")
    plt.title(out_model)
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()

    return model


if __name__ == "__main__":
    main()
