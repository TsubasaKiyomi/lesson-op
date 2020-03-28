# ライブラリ
import os
# import pafhlib
import glob
import shutil

# print(os.path.exists('test.txt'))
# OPERATION-SYSTEMの中にtest.txtは存在するか？。#TureかFalse

# print(os.path.isfile('test.txt'))
# ファイルか確認する.isfile #TureかFalse

# print(os.path.isdir('design'))
# ディレクトリか確認する。 #TureかFalse

# os.rename('test.txt', 'renamed.txt')
# ファイルの名前を変更する


# os.symlink('renamed.txt', 'symlink,txt')
# renameのリンクファイルを作成できる。

# os.mkdir('test_dir')
# ディレクトリ(フォルダ)を作成する

# os.rmdir('test_dir')
# ディレクトリを消す

# pafhlib.Path('empty.txt').touch()
# ファイルの作成。
# os.remove('empty.txt')
# ファイルを削除する。

# os.mkdir('test.dir')
# # test.dirを作成。
# os.mkdir('test.dir/test.dir2')
# test_dirのなかにtest_dir2を作成
# print(os.listdir('test.dir'))
# pathib.Path('test.dir/test.dir2/empty.txt').touch()
# test_dir２の中にファイルを作成する。

# print(glob.glob('test.dir/test.dir2/*'))
# test.dir2の中にどんなファイルがあるのか調べる
# *はファイルの中身全て表示させる。


# shutil.copy('test.dir/test.dir2/empty.txt',
# 'test.dir/test.dir2/empty2.txt')
# print(glob.glob('test.dir/test.dir2/*'))
# test.dir2ディレクトリの中のempty.txtファイルをコピーしtest.dir2ファイルを新しく作成する。


# shutil.rmtree('test.dir')
# 選択フォルダを全て削除する。

print(os.getcwd())
