# url 뒤 / 처리

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>hello flask</h2>"

# ~/pro => ~/pro/
# ~/pro/ => ~/pro/
@app.route('/pro/')
def pro():
    return "<h2>hello flask</h2>"


if __name__ == "__main__":
    app.run(debug=True)
