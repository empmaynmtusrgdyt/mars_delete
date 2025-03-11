from flask import Flask, url_for


app = Flask(__name__)
@app.route('/')
def func():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def prom():
    lst = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.', 
           'Мы сделаем обитаемыми безжизненные пока планеты.', 
           'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(lst)


@app.route('/promotion_image')
def img():
    lst = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.',
           'И начнем с Марса!', 'Присоединяйся!']

    colors = ['color-1', 'color-2', 'color-3', 'color-4', 'color-5']
    colored_lines = [f'<h3 class="{colors[i % len(colors)]}">{line}</h3>' for i, line in
                     enumerate(lst)]
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
                  </head>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')
    }" alt="здесь должна была быть картинка марса">
                    {''.join(colored_lines)}
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')