# 기본 플라스크 탬플릿

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>hello flask</h2>"

if __name__ == "__main__":
    app.run(debug=True)
