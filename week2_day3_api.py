from flask import Flask, request, jsonify
from flask_cors import CORS
import json # JSON を扱うための標準ライブラリを読み込む
import os # OSを扱うための標準ライブラリを読み込む

app = Flask(__name__)
CORS(app)

DATA_FILE = "python-week1/data.json" # 保存用ファイル名

# ファイルが存在する場合、データを読み出し返却する関数
def load_data() :
    if not os.path.exists(DATA_FILE) : # ファイルの有無を確認
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# ファイルに保存する関数
def save_data(data) :
    with open(DATA_FILE, "w") as f :
        json.dump(data, f)

# エラーメッセージを生成し返却する関数
def error(message) :
    return jsonify({"status": "error", "message": message})

# 正常な場合のメッセージを追加して返却する関数
def success(data) :
    data["status"] = "ok" # dict型の data に「"status":"ok"」の要素を追加
    return jsonify(data)

@app.route("/add")
# パラメータを受け取りファイルに追加保存し、成否を返却する関数
def add() :
    name = request.args.get("name")
    score_str = request.args.get("score")

    # name の未入力チェック
    if not name or not score_str:  # 未入力の場合
        return error("name and score are required") 
    
    # score のチェック
    try :
        score = int(score_str)
    except :
        return error("score must be a number") 
    
    data = load_data()

    # 次のIDを決める
    if len(data) == 0 :
        new_id = 1
    else :
        new_id = data[-1]["id"] + 1

    data.append({"id": new_id, "name": name, "score": score})
    save_data(data)

    return success({"message": "saved", "id": new_id})

@app.route("/list")
# ファイルから読み込んだデータを返却する関数
def list_data() :
    data = load_data()

    # 検索機能を追加
    keyword = request.args.get("name")
    if keyword : # 検索ワードがある場合
        data = [r for r in data if keyword.lower() in r["name"].lower()]
    
    # score をキーにしてソート
    sort = request.args.get("sort")
    if sort == "score" : # score の昇順
        data = sorted(data, key = lambda r: r["score"])
    elif sort == "score_desc" : # score の降順
        data = sorted(data, key=lambda r: r["score"], reverse=True)
        
    return success({"records": data})

@app.route("/delete")
# パラメータ(id)を受け取りファイルから削除し、成否を返却する関数
def delete() :
    id_str = request.args.get("id")

    # id が未入力の場合 error
    if not id_str :
        return error("id is required")
    
    # id を数値に変換(数字以外が入力された場合は error)
    try :
        target_id = int(id_str)
    except :
        return error("id must be number")

    data = load_data()

    new_data = [] # 書き込み用の空Listを作成
    found = False # マッチングフラグ(一致する id が見つかったら True)

    for record in data :
        if record["id"] == target_id : # 一致する id が見つかった場合
            found = True
        else :
            new_data.append(record) # 削除しないデータを追加
    
    if not found : # id に一致するものがなかった場合 error
        return error("record not found")
    
    # 削除済みのデータを書き出す
    save_data(new_data)
    return success({"message": "deleted"})

@app.route("/update")
# パラメータ(id)を受け取りファイル名前とスコアを更新し、成否を返却する関数
def update() :
    id_str = request.args.get("id")
    name = request.args.get("name")
    score_str = request.args.get("score")

    # id が未入力の場合 error
    if not id_str :
        return error("id is required")
    
    # id を数値に変換(数字以外が入力された場合は error)
    try :
        target_id = int(id_str)
    except :
        return error("id must be number")

    data = load_data()

    found = False # マッチングフラグ(一致する id が見つかったら True)

    for record in data :
        if record["id"] == target_id : # 一致する id が見つかった場合
            found = True
            # 名前が入力されていれば更新
            if name :
                record["name"] = name
            # スコアに数字が入力されていれば数値変換して更新
            if score_str:
                try :
                    score = int(score_str)
                    record["score"] = score
                except :
                    return error("score must be number")
    
    if not found : # id に一致するものがなかった場合 error
        return error("record not found")
    
    # 更新済みデータを書き出す
    save_data(data)
    return success({"message": "updated"})

app.run()