# 服务器程序 (server.py)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

app.run(port=5000)  # 服务器进程