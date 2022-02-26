csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list(csv):
    data = get_read(csv)
    list_data = sort_age(data)
    result = filter_(list_data)
    return result


def get_read(csv):
    data = [x.split(';') for x in csv.split('\n')]
    return data


def sort_age(data):
    list_data = sorted(data, key=lambda x: int(x[1]))
    return list_data


# Фильтрация
def filter_(list_data):
    filter_data = [x for x in list_data if int(x[1]) > 10]
    return filter_data


if __name__ == '__main__':
    print(get_users_list(csv))