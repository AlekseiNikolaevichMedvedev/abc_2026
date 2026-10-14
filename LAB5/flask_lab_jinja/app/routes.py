import random
from flask import render_template, request, redirect, url_for, session
from app import app
from wheel_of_fortune import WheelOfFortune

# Список слов для случайного выбора при перезапуске
WORDS_POOL = ["якубович", "барабан", "автомобиль", "суперигра", "сектор", "капитал"]

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/page')
def page():
    return render_template('page.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    # Загружаем состояние игры текущего пользователя из сессии
    game_data = session.get('game_state')
    
    if not game_data:
        # Если игры еще нет, создаем новую со случайным словом
        initial_word = random.choice(WORDS_POOL)
        game_instance = WheelOfFortune(word=initial_word, lives=5)
        session['game_state'] = game_instance.to_dict()
    else:
        game_instance = WheelOfFortune.from_dict(game_data)

    message = None
    message_type = "info"

    if request.method == 'POST':
        # Перезапуск игры
        if 'restart' in request.form:
            initial_word = random.choice(WORDS_POOL)
            game_instance = WheelOfFortune(word=initial_word, lives=5)
            session['game_state'] = game_instance.to_dict()
            return redirect(url_for('game'))

        # Ход игрока (ввод буквы)
        letter = request.form.get('letter', '').strip()
        
        if not letter:
            message = "Вы ничего не ввели!"
            message_type = "error"
        elif len(letter) != 1:
            message = "Нужно ввести ровно одну букву!"
            message_type = "error"
        elif game_instance.is_game_over:
            message = "Игра окончена. Начните новую игру."
            message_type = "warning"
        else:
            letter_lower = letter.lower()
            if letter_lower in game_instance.guessed_letters:
                message = f"Буква '{letter.upper()}' уже была названа."
                message_type = "warning"
            else:
                success = game_instance.guess_letter(letter)
                if success:
                    message = f"Есть такая буква! ('{letter.upper()}')"
                    message_type = "success"
                else:
                    message = f"Промах! Буквы '{letter.upper()}' нет в слове."
                    message_type = "error"
                
                # Сохраняем обновленное состояние игры обратно в сессию
                session['game_state'] = game_instance.to_dict()

    return render_template(
        'game.html',
        title='Поле чудес',
        game=game_instance,
        message=message,
        message_type=message_type
    )
