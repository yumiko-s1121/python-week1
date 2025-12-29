from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PASS_LINE = 80

@app.route("/check")
def check() :
    name = request.args.get("name")
    score_str = request.args.get("score")

    if not name or not score_str:
        return jsonify({"error" : "name and score are required"})
    try :
        score = int(score_str)
    except :
        return jsonify({"error":"score must be a number"})
    if score >= PASS_LINE :
        result = "Pass"
        message = f"{name}, you passed!"
    else :
        result = "Fail"
        message = f"{name}, you failed"
    return jsonify({
        "name" : name,
        "score" : score,
        "result" : result,
        "message" : message
    })
app.run()
