from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PASS_LINE = 80

@app.route("/check")
def check() :
    score = int(request.args.get("score"))

    if score >= PASS_LINE :
        result = "Pass"
    else :
        result = "Fail"
    
    return jsonify({"result": result})

app.run()
