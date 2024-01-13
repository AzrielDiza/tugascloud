from flask import Flask, render_template, request

app = Flask(__name__)

# Data game sederhana (gunakan data sesuai kebutuhan)
games = [
    {'title': 'Game A', 'genre': 'Action'},
    {'title': 'Game B', 'genre': 'Adventure'},
    {'title': 'Game C', 'genre': 'RPG'},
]

@app.route('/')
def home():
    return render_template('index.html', games=games)

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form.get('keyword', '').lower()
    result = [game for game in games if keyword in game['title'].lower()]
    return render_template('index.html', games=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
