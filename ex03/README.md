# 第3回
## 迷路ゲーム：迷えるこうかとん（ex03/maze.py）
### ゲーム概要
- ex03/maze.pyを実行すると，1500x900䛾canvasに迷路が描画され，迷路に沿ってこうかとんを移動させるゲーム
- 実行するたびに迷路䛾構造䛿変化する
- イメージとしてゴールで次の階層に行くようなダンジョンみたいなものにした
### 操作方法
- 矢印キーでこうかとんを上下左右に移動する
- Nキーでノーマルモード　道が進める
- Wキーで壁モード　壁が進める
- ゴールでRキーで次の階へ　再描画をする
### 追加機能
- スタート地点とゴール地点䛾追加：スタート地点は（1、1）に固定し緑にしたが、ゴールの位置は三方向が壁の道（行き止まり）のところをゴールの候補としその中からランダムに取り出し、一つをゴールとし赤くした。その際リストの0番に（１，１）が来る可能性が高かったため0番は除いた。
- ゴール判定を実装したためゴールするとメーセージが出てくる。またゴール時にmaze_list（０と１の行列）を全て2にし動けないようにした。
- ゴールして「Rキー」を押すと再描画するようにした。イメージとして次の階層に行くようなダンジョンみたいなものにした。Rキーを押した際新しいmaze_list（０と１の行列）を使い描画し直す．
- 起動時のこうかとんの画像をランダムで取れるようにした
- 「Wキー」を押すと壁モード、「Nキー」を押すとノーマルモードとした。ノーマルモードは基本の道だけを進めるモードとなっている。壁モードは壁の実を進めるものになっている。モードを変えた際、現在の場所が何であろうと表示されなくなることはないが、モードの指定の物しか進めなく、道で壁モードを使った際は隣接する壁には入れるが、道は動けなくなる。
### ToDo（実装しようと思ったけど時間がなかった）
- 自動で動くお邪魔キャラ
- 起動時だけではなく、再起動でもこうかとんの画像を変更したかった。
### メモ