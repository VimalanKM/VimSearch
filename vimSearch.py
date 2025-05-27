from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    return render_template('results.html', query=query)

@app.route('/authorization-code/callback')
def callback():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
