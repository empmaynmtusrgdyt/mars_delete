from flask import Flask, render_template


app = Flask(__name__)

professions = [
    "Пилот",
    "Инженер",
    "Врач",
    "Геолог",
    "Биолог",
    "Программист",
    "Строитель",
    "Специалист по жизнеобеспечению",
]


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    return render_template('base.html',
                           title='Список профессий',
                           list_type=list_type,
                           professions=professions)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')