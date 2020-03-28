import csv

# with open('test.csv', 'w') as csv_file:

# fieldnames = ['Name', 'Count']
# フィールド名　['Name', 'Count']がcsv上で出力される。

# writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
# writerオブジェクトを作成　第一引数にcsv　第二引数にfieldnamesを入れる。

# writer.writeheader()
# .writeheader書き込みヘッダー

####ここから書き込み内容#####
# writer.writerow({'Name': 'A', 'Count': 1})
# writer.writerow({'Name': 'B', 'Count': 2})
# writer.writerow({'Name': 'C', 'Count': 3})
# test.csvに表示される。

#####ここから読み込み内容####
with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])
