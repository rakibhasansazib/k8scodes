from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Congrates!!! you deployed apps on k8s successfully.'
