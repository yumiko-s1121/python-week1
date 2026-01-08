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
def error(message, code = 400) :
    return jsonify({"status": "error", "message": message}), code

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
        return error("name and score are required") # 返却値を変更
    
    # score のチェック
    try :
        score = int(score_str)
    except :
        return error("score must be a number") # score に数値以外が入力された場合 error
    
    # score の範囲チェック(0〜100)
    if score < 0 or score > 100 :
        return error("score must be between 0 and 100") # 範囲外の場合 error
    
    data = load_data()
    # List に追加
    data.append({"name": name, "score": score}) # data(List型)の各要素がdict型になっている
    save_data(data)

    return success({"message": "saved"}), 201

@app.route("/update")
# パラメータを受け取り該当データを更新し、成否を返却する関数
def update() :
    name = request.args.get("name")
    score_str = request.args.get("score")

    # name の未入力チェック
    if not name or not score_str:  # 未入力の場合
        return error("name and score are required") # 返却値を変更
    
    # score のチェック
    try :
        score = int(score_str)
    except :
        return error("score must be a number") # score に数値以外が入力された場合 error
    
    # score の範囲チェック(0〜100)
    if score < 0 or score > 100 :
        return error("score must be between 0 and 100") # 範囲外の場合 error
    
    data = load_data()

    # 該当データを探索し、更新
    for row in data :
        # 該当データが見つかったら更新して終了
        if (row["name"] == name) :
            row["score"] = score
            save_data(data)
            return success({"message": "update"})
    
    # 見つからなかった場合
    return error("record not found", 404)


@app.route("/list")
# ファイルから読み込んだデータを返却する関数
def list_data() :
    data = load_data()
    return success({"records": data})

app.run()
