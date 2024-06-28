from flask import Flask, request, render_template, jsonify, session
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'  # This stores sessions on the filesystem
Session(app)

@app.route('/')
def index():
    if 'data' not in session:
        session['data'] = []
    return render_template('index.html', data=session['data'])

@app.route('/submit', methods=['POST'])
def submit():
    if 'data' not in session:
        session['data'] = []
    new_entry = request.form.to_dict()
    session['data'].append(new_entry)
    session.modified = True  # Make sure session is updated
    return jsonify(data=session['data'])

if __name__ == '__main__':
    app.run(debug=True)
