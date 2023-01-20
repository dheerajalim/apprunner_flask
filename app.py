from flask import Flask, jsonify
from waitress import serve

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    data = {
                "Service " : 'App Runner',
                "Message" : "You Flask App is succesfuly deployed using App Runner ",
            }

    return jsonify(data)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
