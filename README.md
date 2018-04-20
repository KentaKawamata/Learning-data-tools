# 使用環境

||
|:--|
|Ubuntu14.04 LTS or 16.04 LTS|
|anaconda3.4 or 3.5|
|Python 3.X|
|OpenCV 3.X|
|Keras 2.X|
|tqdm 4.19.9 |

## Rename.py

各画像データの名称変更.
`python Rename.py`

## extract.py

特定のディレクトリから画像をランダムで抽出.
`python extract.py`

## image_generator.py

KerasのImageDataGeneratorを用いて学習データを水増し.
`python image_generator.py`

## process.py

学習に使用する全画像データのパスをテキストファイルに記録.
darknetに画像パスを指定する際に使用.
`python process.py`

## reformat.py

画像の拡張子をdarknetに対応
`python reformat.py`
