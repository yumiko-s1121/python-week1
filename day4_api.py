from flask import Flask, request, jsonify

app = Flask(__name__)

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
