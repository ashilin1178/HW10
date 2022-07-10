from flask import Flask
from utils import load_candidates, get_all

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
    return f'<pre> {all_candidates} </pre>'


if __name__ == "__main__":
    app.run(host='127.0.0.2', port=80)
