from flask import Flask, render_template, url_for
import sys
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/test')
def clickOnBox():
    print('Hello world!', file=sys.stderr)
    app.logger.info("test")
    return ("nothing")

if __name__ == "__main__":
    app.run(debug=True)