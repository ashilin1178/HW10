from flask import Flask
from utils import load_candidates, get_all, get_by_pk, get_by_skill

app = Flask(__name__)

file_name = 'candidates.json'

candidates = load_candidates(file_name)


@app.route('/')
def print_all():
    """
    выводит данные всех кандидатов
    :return:
    """
    all_candidates = get_all(candidates)
    return f'<pre>{all_candidates}</pre>'


@app.route('/candidates/<int:pk>')
def print_candidat(pk):
    """
    выводит данные всех кандидатов
    :return:
    """
    candidat = get_by_pk(candidates, pk)

    return f'<img scr = {candidat["picture"]}<br>'\
           f'<pre>Имя кандидата - {candidat["name"]}<br>'\
           f'Позиция кандидата - {candidat["position"]}<br>'\
           f'Навыки через запятую - {candidat["skills"]}'\
           f'</pre>'


if __name__ == "__main__":
    app.run(host='127.0.0.2', port=80)
