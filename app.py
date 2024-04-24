from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loja')
def loja():
    return render_template('loja.html')

if __name__ == '__main__':
    app.run(debug=True)
