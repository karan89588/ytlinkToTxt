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
        resp,target_lang = getResp(ytlink)
        if(resp!='na'):
            return jsonify({"msg": resp, "success": True,'target_lang':target_lang})
        else:
            return jsonify({'msg':'Opps!!! Either link is incorrect or transcript is disable.','success':False})
    except:
        return jsonify({"msg": "No Transcript Available", "success": False})




if __name__ == "__main__":
    app.run(debug=True)
