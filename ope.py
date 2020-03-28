s = "AAABBBCCCDDD"

with open('test.txt', 'w+') as f:
    f.write(s)
    f.seek(0)
    print(f.read())
"""
with open('test.txt', 'w+') as f:
#書き込みと読み込みをしたい時に　w+　とする。 w[書き込み]　+[プラス読み込みの意味]
#書き込みはできるけど、読み込みはまだできない。

    f.write(s)
#f.write(s)で書き込んだのはDDDの最後なのでseekで先頭に戻り読み込みをさせなければ、出力されない。
    
    f.seek(0)
#f.seekで先頭に戻らないと、読み込みされないので注意。

    print(f.read())
"""
# while True:
#     chunk = 2
#     line = f.read(chunk)
#     print(line)
#     if not line:
#         break

# print(f.tell())
# print(f.read(1))
# f.seek(5)
# print(f.read(1))

# f = open('test.txt', 'a')
# f.write('Test\n')
# print('I am print', file=f)
# f.close()
