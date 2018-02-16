from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('j2_query.html')

@app.route('/process', methods=['POST'])
def process():
    _username = request.form['username']
    if _username:
        return render_template('j2_response.html', username=_username)
    else:
        return 'Please go back and enter a username...',404






'''
@app.route("/")
def index():
    return 'sneaky snake'

@app.route('/test1')
def test1():
    return '<h1>This is the test1 page</h1>'

@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html", name=username)
'''
if __name__ == "__main__":
    app.run(debug=True)