from flask import Flask
from flask import redirect,request,url_for,render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')


@app.route("/post/1", methods=["GET"])
def post():
    return render_template('post1.html')


@app.route("/about", methods=["GET"])
def about():
    return render_template('about.html')


@app.route("/contact", methods=["GET"])
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
