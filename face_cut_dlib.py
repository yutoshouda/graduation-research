import cv2
import dlib
from pathlib import Path
import imutils
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb

names = ['KannaHashimoto', 'AyamiNakajou', 'MinamiHamabe', 'MoneKamishiraishi', 'HanaSugisaki',
         'EikoKoike', 'SuzuHirose', 'NanaMori', 'TaouTsuchiya',
         'TomoyaNakamura', 'MasakiSuda', 'GouAyano', 'RyouYoshizawa', 'HiroshiAbe',
         'MakkenyuArata', 'RyuseiYokohama', 'MasatoSakai', 'TatsuyaFujiwara'
         ]

for name in names:
    indir = Path("./data/" + name + "/")
    outdir = Path("./face/" + name + "/")
    print(indir)
    print(outdir)

    outdir.mkdir(parents=True, exist_ok=True)

    images = []
    for img_name in indir.glob("*"):
        images.append(img_name)

    face_predictor = "./cascade_file/shape_predictor_68_face_landmarks.dat"

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(face_predictor)
    fa = FaceAligner(predictor, desiredFaceWidth=256)

    print(images)
    for img_name in images:
        print(img_name)
        outfile = outdir / ("%s.jpg" % img_name.stem)
        img = cv2.imread(str(img_name))

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector(img_gray, 2)

        if len(faces) == 0:
            print("==0", img_name)
            continue
        if len(faces) > 1:
            print(">1", img_name)
            continue

        (x, y, w, h) = rect_to_bb(faces[0])
        if w == 0 or h == 0:
            continue

        x = max(0, x)
        y = max(0, y)
        w = min(img_gray.shape[1], x + w) - x
        h = min(img_gray.shape[0], y + h) - y

        faceOrig = imutils.resize(img[y:y + h, x:x + w], width=256)
        faceAligned = fa.align(img, img_gray, faces[0])

        cv2.imwrite(str(outfile), faceAligned)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
