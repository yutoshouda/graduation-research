// getUserMedia が使えないときは、『getUserMedia()が利用できないブラウザです！』と言ってね。
if (typeof navigator.mediaDevices.getUserMedia !== 'function') {
    const err = new Error('getUserMedia()が利用できないブラウザです！');
    alert(`${err.name} ${err.message}`);
    throw err;
}



// 操作する画面エレメント変数定義します。
const $start = document.getElementById('start_btn'); // スタートボタン
const $video = document.getElementById('video_area'); // 映像表示エリア
//const $download = document.getElementById('downloadBtn'); // ダウンロードボタン 

//カメラ表示機能
navigator.mediaDevices.getUserMedia({
        video: true,
        audio: false
    })
    .then(stream => $video.srcObject = stream)
    .catch(err => alert(`${err.name} ${err.message}`));

$(this).blur();

$('tab1').hi


// 「撮影」ボタンが押されたら「<canvas id="capture_image">」に映像のコマ画像を表示します。
function copyFrame() {

    const canvas = document.getElementById('capture_image');
    var cci = canvas.getContext('2d');
    var va = document.getElementById('video_area');

    canvas.width = va.videoWidth;
    canvas.height = va.videoHeight;
    cci.drawImage(va, 0, 0); // canvasに『「静止画取得」ボタン』押下時点の画像を描画。
}

//ダウンロード処理

function downloadFrame_G() {
    let canvas1 = document.getElementById("capture_image");

    let link = document.createElement("a");
    link.href = capture_image.toDataURL("image/JPEG");
    link.download = "test.jpeg";
    link.click();

    location.href = "3page_loding_G.html"
}
function downloadFrame_S() {
    let canvas1 = document.getElementById("capture_image");

    let link = document.createElement("a");
    link.href = capture_image.toDataURL("image/JPEG");
    link.download = "test.jpeg";
    link.click();

    location.href = "3page_loding_S.html"
}

