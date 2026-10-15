from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Главная страница</h1>'

@app.route('/about')
def about():
    return '<h1>О компании</h1><p>Информация о нашей компании.</p>'

@app.route('/contacts')
def contacts():
    return '<h1>Контакты</h1><p>email: info@example.com</p>'

@app.route('/posts')
def posts_list():
    posts = ['Первый пост', 'Второй пост', 'Третий пост']
    posts_html = ''.join(f'<li>{post}</li>' for post in posts)
    return f'<h1>Список постов</h1><ul>{posts_html}</ul>'

if __name__ == '__main__':
    app.run(debug=True)
