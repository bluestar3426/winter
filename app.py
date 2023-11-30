from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>/")
def hello(name):
    return f"Hello, <script>alert('{name}')</script>"

@app.route('/text/')
def text():
    return '<html><body><h1>Hello World</h1></body></html>'

@app.route('/news/')
def hello_name():
    return render_template('hello.html')