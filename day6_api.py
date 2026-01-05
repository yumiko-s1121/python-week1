from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# PASS_LINE = 80
DEFAULT_PASS_LINE = 80

@app.route("/check")
def check() :
    name = request.args.get("name")
    score_str = request.args.get("score")
    pass_line_str = request.args.get("passline")

    # name の未入力チェック
    if not name or not score_str:
        return jsonify({"error": "name and score are required"}) # 未入力の場合
    
    # score のチェック
    try :
        score = int(score_str)
    except :
        return jsonify({"error": "score must be a number"}) # 未入力または数字以外が入力された場合
    
    # passline のチェック
    if pass_line_str :
        try :
            pass_line = int(pass_line_str)
        except :
            return jsonify({"error": "passline must be a number"})
    else :
        pass_line = DEFAULT_PASS_LINE
    
    if score >= pass_line :
        result = "Pass"
        message = f"{name}, you passed!"
    else :
        result = "Fail"
        message = f"{name}, you failed"
    return jsonify({
        "name" : name,
        "score" : score,
        "passline" : pass_line,
        "result" : result
    })
app.run()
