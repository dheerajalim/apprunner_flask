from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    data = {
                "Service " : 'App Runner',
                "Message" : "You Flask App is succesfuly deployed using App Runner ",
            }
    
    return jsonify(data)