from flask import Flask, request, jsonify
from flask_cors import CORS
import json # JSON を扱うための標準ライブラリを読み込む
import os # OSを扱うための標準ライブラリを読み込む

app = Flask(__name__)
CORS(app)

DATA_FILE = "data.json" # 保存用ファイル名

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
        return error("name and score are required") # 返却値を変更
    
    # score のチェック
    try :
        score = int(score_str)
    except :
        return error("score must be a number") # 返却値を変更
    
    data = load_data()
    data.append({"name": name, "score": score})
    save_data(data)

    return success({"message": "saved"})

@app.route("/list")
# ファイルから読み込んだデータを返却する関数
def list_data() :
    data = load_data()
    return success({"records": data})

app.run()