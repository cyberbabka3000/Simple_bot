import datetime


def cur_week():
    today = datetime.datetime.today()
    week_num = today.isocalendar()[1]
    if week_num % 2 == 0:
        return "Чётная"
    else:
        return "Нечётная"


def cur_week_for_db(x):
    if x == 1:
        if cur_week() == "Нечётная":
            return 1
        else:
            return 2
    if cur_week() == "Нечётная":
        return 2
    else:
        return 1