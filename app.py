from flask import Flask, request, jsonify
from flask_cors import CORS
from getTranscriptTY import getResp



app = Flask(__name__)



CORS(app)


@app.route("/", methods=["GET"])
def get():
    return jsonify({"msg": "Hello"})


@app.route("/getTranscript", methods=["POST"])
def createUser():
    try:
        ytlink = request.json["ytlink"]
        resp = getResp(ytlink)
        return jsonify({"msg": resp, "success": True})
    except:
        return jsonify({"msg": "No Transcript Available", "success": False})




if __name__ == "__main__":
    app.run(debug=True)
