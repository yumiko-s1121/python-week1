import csv

with open("python-week1/data.csv") as f:
    reader = csv.reader(f)
    header = next(reader) # 1行目を読み込む

    results = []

    for row in reader : # 2行目以降を読み込んで処理
        name = row[0]
        score = int(row[1])

        if score >= 80 :
            result = "Pass"
        else :
            result = "Fail"
        
        results.append([name, score, result])

print(results)

with open("python-week1/result.csv", "w", newline="") as f:
    writer = csv.writer(f)

    # ヘッダー
    writer.writerow(["name", "score", "result"])

    # データ
    for row in results :
        writer.writerow(row)
print("result.csv created")