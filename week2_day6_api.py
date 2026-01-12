from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector # MySQL 接続用のライブラリを読み込む

app = Flask(__name__)
CORS(app)

# DB の設定
DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "root1234"
DB_NAME = "score_app"

# DB に接続する関数
def get_conn() :
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

# エラーメッセージを生成し返却する関数
def error(message) :
    return jsonify({"status": "error", "message": message})

# 正常な場合のメッセージを追加して返却する関数
def success(data) :
    data["status"] = "ok" # dict型の data に「"status":"ok"」の要素を追加
    return jsonify(data)

@app.route("/login")
# ログイン機能を提供する関数
def login() :
    #パラメータを取得
    username = request.args.get("username")
    password = request.args.get("password")

    if not username or not password :
        return error("username and password are required")

    conn = get_conn() # コネクションを取得
    cur = conn.cursor(dictionary=True) # カーソルを取得

    sql = "select id from users where username = %s and password = %s"
    cur.execute(sql, (username, password)) # SQL を実行

    user = cur.fetchone()

    cur.close()
    conn.close()

    if not user :
        return error("Invalid login")
    
    return success({"message": "login ok", "user_id": user["id"]})


@app.route("/add")
# パラメータを受け取りデータベースに追加し、ID を返却する関数
def add() :
    # パラメータを取得
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
    
    sql = "insert into scores (name, score) values (%s, %s)" # 実行する SQL

    try :
        conn = get_conn() # コネクションを取得
        cur = conn.cursor() # カーソルを取得

        cur.execute(sql, (name, score)) # SQL を実行

        conn.commit() # 更新を確定する
        new_id = cur.lastrowid # 自動採番された番号を取得

    except mysql.connector.Error as e:
        if "unique" in str(e).lower():
            return error("This name already exists")
        if "check" in str(e).lower():
            return error("Score must be between 0 and 100")
        return error("Database error")
            
    finally :
        # カーソルの解放とDB切断
        cur.close()
        conn.close()

    return success({"message": "saved", "id": new_id})

@app.route("/list")
# 検索結果を指定された順で整列して一覧で表示する関数
def list_data() :
    # パラメータを取得
    keyword = request.args.get("name")
    sort = request.args.get("sort")

    sql = "select id, name, score from scores" # 実行する SQL
    params = [] # プレースホルダーの値
   
    # 検索条件を追加
    if keyword :
        sql += " where lower(name) like %s"
        params.append(f"%{keyword.lower()}%")
    
    # 整列の指定を追加
    if sort == "score" :
        sql += " order by score"
    elif sort == "score_desc" :
        sql += " order by score desc"
    else :
        sql += " order by id"

    conn = get_conn() # コネクションを取得
    cur = conn.cursor(dictionary=True) # カーソルを取得

    cur.execute(sql, params) # SQL を実行
    rows = cur.fetchall() # 結果表を取得

    # カーソルの解放とDB切断
    cur.close()
    conn.close()

    return success({"records": rows})
    
@app.route("/delete")
# 指定された ID のレコードを DB から削除
def delete() :
    # パラメータを取得
    id_str = request.args.get("id")

    # 入力値エラーチェック
    if not id_str : # 未入力チェック
        return error("id is required")
    
    try :  # 数値チェック
        target_id = int(id_str)
    except :
        error("id must be number")

    sql = "delete from scores where id = %s" # 実行する SQL
   
    conn = get_conn() # コネクションを取得
    cur = conn.cursor(dictionary=True) # カーソルを取得

    cur.execute(sql, (target_id,)) # SQL を実行
    conn.commit() # 更新を確定する

    delete = cur.rowcount # 削除した行数を取得

    # カーソルの解放とDB切断
    cur.close()
    conn.close()

    # 該当レコードが存在しない場合
    if delete == 0 :
        return error("record not found")

    return success({"message": "delete"})

@app.route("/update")
def update() :
    # パラメータを取得
    id_str = request.args.get("id")
    name = request.args.get("name")
    score_str = request.args.get("score")

    # 入力値エラーチェック
    if not id_str : # 未入力チェック
        return error("id is required")
    
    try :  # 数値チェック
        target_id = int(id_str)
    except :
        return error("id must be number")

    # 更新内容の有無をチェック
    if (name is None or name == "") and (score_str is None or score_str == "") :
        return error("nothing to update")

    # SQL の設定
    fields = [] # 更新するフィールド
    params = [] # 更新する値

    if name : # name を変更する場合
        fields.append = ("name = %s")
        params.append = (name)
    
    if score_str : # score を変更する場合
        try :
            score = int(score_str)
        except :
            return error("score must be number")
        fields.append("score = %s")
        params.append(score)

    params.append(target_id)

    sql = f"update scores set {','.join(fields)} where id = %s" # 実行する SQL
   
    conn = get_conn() # コネクションを取得
    cur = conn.cursor(dictionary=True) # カーソルを取得

    cur.execute(sql, params) # SQL を実行
    conn.commit() # 更新を確定する

    update = cur.rowcount # 削除した行数を取得

    # カーソルの解放とDB切断
    cur.close()
    conn.close()

    # 該当レコードが存在しない場合
    if update == 0 :
        return error("record not found")

    return success({"message": "update"})

app.run()