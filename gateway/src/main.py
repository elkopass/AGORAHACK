from flask import Flask

from publisher import publish_forever

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    publish_forever()
#     app.run(host="0.0.0.0", debug=True)
  
