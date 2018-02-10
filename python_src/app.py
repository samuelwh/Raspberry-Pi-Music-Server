from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return 'sneaky snake'

@app.route('/test1')
def test1():
    return '<h1>This is the test1 page</h1>'

@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html", name=username)

if __name__ == "__main__":
    app.run(debug=True)