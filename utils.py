from json import load

file_name = "candidates.json"


def load_candidates(file_name_: str):
    """
    функция загружает данные из файла в список
    """
    with open(file_name_, "r", encoding="UTF8") as file:
        candidates_ = load(file)

    return candidates_


def get_all(candidates_: list):
    """
    выводит данные всех кандидатов
    :param candidates_:
    :return:
    """
    for candidat in candidates_:
        return candidat


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
    функция возвращает кандидатов по навыку
    :param candidates_:
    :param skill_name:
    :return:
    """
    result = []
    for candidat in candidates_:
        if skill_name.lower() in candidat["skills"].lower():
            result.append(candidat)
    return result


candidates = load_candidates(file_name)
#get_by_skill(candidates, 'Delphi')
print(get_by_skill(candidates, 'Python'))

