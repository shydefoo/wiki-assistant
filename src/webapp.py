from flask import Flask
from flask import request, Response

app = Flask(__name__)

@app.route('/')
def homepage():
    return Response("Hello world")





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False)
