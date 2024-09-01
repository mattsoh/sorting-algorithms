from flask import Flask, make_response, request
from flask_cors import CORS
import json
import sorts

app = Flask(__name__)
CORS(app)
@app.route("/test")
def test():
    return "Hello, World!"
@app.route("/query")
def index():
    try:
        option = request.args.get("type")
        lst = json.loads(request.args.get("list"))
        if not isinstance(lst, list):
            print("Invalid list")
            return
        res = sorts.getTime(option, lst)
        print(res)
        return json.dumps(res)
    except json.JSONDecodeError as error:
        return make_response("Invalid List", 403)
    except:
        return make_response("Invalid List", 403)
    # return type
if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)