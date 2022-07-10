from json import load


def load_candidates(file_name_: str):
    """
    функция загружает данные из файла в список
    """
    with open(file_name_, "r", encoding="UTF8") as file:
        candidates_ = load(file)

    return candidates_


def get_all(candidates_):
    """
    выводит данные всех кандидатов
    :param candidates_:
    :return:
    """
    all_cadidates = ""
    for candidat in candidates_:
        all_cadidates += f'Имя кандидата - {candidat["name"]}<br>' \
                         f'Позиция кандидата - {candidat["position"]}<br>' \
                         f'Навыки через запятую - {candidat["skills"]}<br><br>'
    return all_cadidates


def get_by_pk(candidates_, pk):
    """
    возвращает кандидата по pk
    :param candidates_: 
    :param pk:
    :return:
    """
    for candidat in candidates_:
        if pk == candidat["pk"]:
            return candidat


def get_by_skill(candidates_, skill_name):
    """
    функция возвращает кандидатов по заданному навыку
    :param candidates_:
    :param skill_name:
    :return:
    """
    result = []

    for candidat in candidates_:
        # преобразуем строку с навыками в список и убираем пробелы
        skill_ = candidat['skills'].lower().replace(' ', '').split(",")
        # подготавливаем запрос по скилам для условия, убираем пробелы и переводим в нижний регистр
        skill_name_for_if = skill_name.replace(' ', '').lower()

        if skill_name_for_if in skill_:
            result.append(candidat)

    return result


can = load_candidates("candidates.json")

print(get_by_skill(can, 'обсуждать важные вопросы'))
