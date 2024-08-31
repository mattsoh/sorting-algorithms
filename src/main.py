from flask import Flask, request
import json
import sorts

app = Flask(__name__)
@app.route("/test")
def test():
    return "Hello, World!"
@app.route("/query")
def index():
    try:
        type = request.args.get("type")
        lst = json.loads(request.args.get("list"))
        # return isinstance(lst, int)
        if not isinstance(lst, list):
            print("Invalid list")
            return
        print(type, lst)
        print(sorts.getTime(type, lst))
    except json.JSONDecodeError as error:
        print("Invalid list")
    return type
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)