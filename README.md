# minecraft_get_building
マイクラ内の建造物をcsv化する\
This program convert building in minecraft to csv file.

#動作環境 Environment
Minecraft Java Edition v1.12.2\
Forge 14.23.5.2855\
Raspberry Jam Mod 0.92

#使い方 Usage
pipコマンドでインストール
```commandline
pip install minecraft_get_building
```

・コマンドラインから
```commandline
minecraft_get_building x y z x_range y_range z_range --output_path --get_blocks --ignore_blocks
```
x,y,z:建造物の角の座標　各値は最小値\
x_range,y_range,z_range:x,y,z方向の建造物のサイズ\
--output_path:csvの出力先のパス\
--get_blocks:取得するブロックの指定 [[id_1, data_1], [id_2,data_2],...]\
--ignore_blocks::取得しないブロックの指定 [[id_1, data_1], [id_2,data_2],...]\

・スクリプト内で使用
```python
from minecraft_get_building import get_building_data

get_building_data.get_building_data(
    x,
    y,
    z,
    x_range,
    y_range,
    z_range,
    output_path=None,
    get_blocks=None,
    ignore_blocks=None,
)
```
引数はコマンドラインからと同じ
