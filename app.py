from flask import Flask, render_template

app = Flask(__name__)

@app.route('/mypage/me')
def me():
    return render_template('me.html')

@app.route('/mypage/contact')
def contact():
    return render_template('contact.html')

@app.route('/')
def base():
    return render_template('base.html')

