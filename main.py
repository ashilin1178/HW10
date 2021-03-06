from flask import Flask
from utils import load_candidates, get_all, get_by_pk, get_by_skill


def main():
    app = Flask(__name__)
    # Файл с кандидатами
    file_name = 'candidates.json'
    # Загружаем данные из файла
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
    def print_candidat_by_pk(pk):
        """
        выводит данные кандидата по номеру pk
        :param pk:
        :return:
        """
        candidat = get_by_pk(candidates, pk)
        url = candidat['picture']
        return f'<img src = "{url}"><br>' \
               f'<pre>Имя кандидата - {candidat["name"]}<br>' \
               f'Позиция кандидата - {candidat["position"]}<br>' \
               f'Навыки через запятую - {candidat["skills"]}' \
               f'</pre>'

    @app.route('/skills/<skill>')
    def print_candidates_by_skill(skill):
        """
        выводит кандидатов с заданным навыком
        :param skill:
        :return:
        """
        candidates_with_skill = get_by_skill(candidates, skill)
        result = ""
        for candidat in candidates_with_skill:
            result += f'Имя кандидата - {candidat["name"]}<br>' \
                      f'Позиция кандидата - {candidat["position"]}<br>' \
                      f'Навыки через запятую - {candidat["skills"]}<br><br>'

        return f'<pre>{result}</pre>'

    app.run()


if __name__ == "__main__":
    main()
