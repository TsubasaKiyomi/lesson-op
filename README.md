### open

- file を開き、対応するファイルオブジェクトを返す。
- ファイルを開くことができなければ、OSError となる。

```
f = opne()
()内にはファイル名とファイルが開かれるmode,モードを指定する。
```

##### モードの種類

'r' 読み込み用に開く（デフォルト）
'w' 書き込みように開く、まずファイルを切り詰める
'x' 排他的な生成に開き、ファイルが存在する場合は失敗する。
'a' 書き込み用に開き、ファイルが存在する場合は末尾に追記する。
'b'バイナリモード
't'テキストモード
'+' open for updating (reading and writing)

read()
ファイルのデータをすべて読み込む。
返り値は、文字列。
read(n)
ファイルのデータを n バイト分読み込む。
write(s)
文字列またはリスト s をファイルに書き込む。
close()
ファイルを閉じる。

#### バイナリとは

2 進数で表されるもの
テキストデータ以外のデータ（バイナリデータ）のこと。またはバイナリファイルのこと。

```
f = open('test', 'w')
f.write('Test\n')
print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
f.close()

```

f = open('test', 'w')

- open()関数で新しくファイルの作成コード file として管理される。

f.write('Test\n')

- 新しく作成したファイルに Test を書き込み保存(出力)

print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)

- print でも出力できる。

f.close()

- 書き込み作業終了宣言

- open()したファイルオブジェクトは close()メソッドでクローズする必要がある。

#### close 閉じ忘れが無いように

with ステートメントを使用する

```
with open('test,test', 'w') as f:
    f.write('Test\n')
```

- with open( ) as xxxx: の xxxx には任意の名前を使用できる。

### seek

◯ 文字目に戻ったり、◯ 文字目を読み込みたい時に使用する。

#### 読み込みと書き込み W+ r+

```
s = "AAABBBCCCDDD"

with open('test.txt', 'w+') as f:
with open('test.txt', 'r+') as f:
    f.write(s)
    f.seek(0)
    print(f.read())
"""
with open('test.txt', 'w+') as f:
#書き込みと読み込みをしたい時に　w+　とする。 w[書き込み]　+[プラス読み込みの意味]
#書き込みはできるけど、読み込みはまだできない。

#with open('test.txt', 'r+') as f:
#読み込みと書き込みをしたい時は　r+ とする。読み込むファイルが無いとエラーとなる。

    f.write(s)
#f.write(s)で書き込んだのはDDDの最後なのでseekで先頭に戻り読み込みをさせなければ、出力されない。

    f.seek(0)
#f.seekで先頭に戻らないと、読み込みされないので注意。

    print(f.read())
"""
```

#### CSV ファイルへの書き込みと読み込み

- csv ファイルは「,」カンマ区切りの text ファイル形式のこと。開くと Excel などになる。
