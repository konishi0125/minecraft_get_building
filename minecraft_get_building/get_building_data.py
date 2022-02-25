"""
マイクラの建造物をcsvデータに変換する
"""

import argparse
import csv
import mcpi.minecraft as minecraft


def get_building_data(
    x,
    y,
    z,
    x_range,
    y_range,
    z_range,
    output_path=None,
    get_blocks=None,
    ignore_blocks=None,
):
    """
    建造物をcsvデータとして出力する
    :param x: 建造物の角 x座標の最小値
    :param y: 建造物の角 y座標の最小値
    :param z: 建造物の角 z座標の最小値
    :param x_range: 建造物の大きさ x方向
    :param y_range: 建造物の大きさ y方向
    :param z_range: 建造物の大きさ z方向
    :param output_path: csvの出力先
    :param get_blocks: 取得するブロックの種類を限定する ブロックidのリスト
    :param ignore_blocks: 取得しないブロックの種類を指定する ブロックidのリスト
    :return: out ブロックの位置と種類のリスト
    """

    # mcpi init
    mc = minecraft.Minecraft.create()

    if get_blocks is not None:
        get_blocks = check_and_convert_blocks_list(get_blocks)
    if ignore_blocks is not None:
        ignore_blocks = check_and_convert_blocks_list(ignore_blocks)

    out = [["x", "y", "z", "id", "data"]]
    for y_ in range(y_range):
        for x_ in range(x_range):
            for z_ in range(z_range):
                x_pos = x + x_
                y_pos = y + y_
                z_pos = z + z_
                block = mc.getBlockWithData(x_pos, y_pos, z_pos)
                if get_blocks is not None:
                    if judge_get_block(get_blocks, block) is False:
                        continue
                if ignore_blocks is not None:
                    if judge_get_block(ignore_blocks, block) is True:
                        continue
                out.append([x_, y_, z_, block.id, block.data])

    if output_path is not None:
        print(f"csvを出力します -> {output_path}")
        with open(output_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(out)

    return out


def check_and_convert_blocks_list(blocks_list):
    """
    get_blocks, ignore_blocksが適切な型かどうかの判断
    型が間違っていればプログラム終了
    合っていればint型に変換
    :param blocks_list: get_blocks, ignore_blocks
    :return: int型に変換したblock_list
    """

    int_blocks_list = []
    for block in blocks_list:
        if type(block) != list or len(block) != 2:
            print("get_blocksもしくはignore_blocksが適切な型ではありません")
            print(
                "get_blocks,ignore_blocks -> [[id_1, data_1], [id_2, data_2], ... ,[id_n, data_n]]"
            )
            print("プログラムを終了します")
            exit()
        int_blocks_list.append([int(block[0]), int(block[1])])
    return int_blocks_list


def judge_get_block(get_blocks, target_block):
    """
    取得するブロックかどうかの判定
    :param get_blocks: 取得するブロックの種類を限定する ブロックid,dataのリスト
    :param target_block: minecraft内で配置されているブロック
    :return: target_blockがget_blocksに含まれているならTrue、含まれていないならFalse
    """
    for get_block in get_blocks:
        if get_block[0] == target_block.id and get_block[1] == target_block.data:
            return True
    return False


def judge_ignore_block(ignore_blocks, target_block):
    """
    取得しないブロックかどうかの判定
    :param ignore_blocks: 取得しないブロックの種類を指定する ブロックidのリスト
    :param target_block: minecraft内で配置されているブロックid
    :return: target_blockがignore_blocksに含まれているならFalse、含まれていないならTrue
    """
    for ignore_block in ignore_blocks:
        if ignore_block[0] == target_block.id and ignore_block[1] == target_block.data:
            return False
    return True


def main():
    """
    コマンドラインで動くときの関数
    :return:
    """

    def replace_list_convert_to_int(blocks):
        blocks = blocks[1:-1].split("[")[1:]
        int_blocks = []
        for block in blocks:
            block = block.replace("]", "").split(",")
            int_blocks.append([int(block[0]), int(block[1])])
        return int_blocks

    parser = argparse.ArgumentParser()
    parser.add_argument("x", help="建物の角のx座標", type=int)
    parser.add_argument("y", help="建物の角のy座標", type=int)
    parser.add_argument("z", help="建物の角のz座標", type=int)
    parser.add_argument("x_range", help="建物のx方向の大きさ", type=int)
    parser.add_argument("y_range", help="建物のy方向の大きさ", type=int)
    parser.add_argument("z_range", help="建物のz方向の大きさ", type=int)
    parser.add_argument("-p", "--output_path", help="csvの出力先")
    parser.add_argument("-g", "--get_blocks", help="取得するブロックの種類")
    parser.add_argument("-i", "--ignore_blocks", help="取得しないブロックの種類")

    args = parser.parse_args()

    if args.get_blocks is not None:
        args.get_blocks = replace_list_convert_to_int(args.get_blocks)
    if args.ignore_blocks is not None:
        args.ignore_blocks = replace_list_convert_to_int(args.ignore_blocks)

    get_building_data(
        args.x,
        args.y,
        args.z,
        args.x_range,
        args.y_range,
        args.z_range,
        output_path=args.output_path,
        get_blocks=args.output_path,
        ignore_blocks=args.output_path,
    )


if __name__ == "__main__":
    main()
