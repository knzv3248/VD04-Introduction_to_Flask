from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Главная")

@app.route('/blog')
def blog():
    return render_template('blog.html', title="Блог")

@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title="Контакты")

if __name__ == '__main__':
    app.run(debug=True)
