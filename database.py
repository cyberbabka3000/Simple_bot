import psycopg2

conn = psycopg2.connect(database="timetable",
                        user="postgres",
                        password="000",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()

weekday = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']


def get_day(week, day):
    timetable = [0] * 5
    cursor.execute(f'SELECT class, room, time FROM timetable_l WHERE week = {week} AND day = {day}')
    clas = cursor.fetchall()
    print(clas)
    for cl in clas:
        day1 = []
        cursor.execute(f'SELECT subject, subject_type FROM class WHERE id = {cl[0]}')
        subjects = cursor.fetchall()
        subject = subjects[0][0]
        subject_type = subjects[0][1]
        cursor.execute(f'SELECT time FROM time_start WHERE id_time = {cl[2]}')
        time = cursor.fetchone()[0]
        day1.append(time)
        cursor.execute(f'SELECT subject FROM subject WHERE id_Предмета = {subject}')
        subj = cursor.fetchone()[0]
        day1.append(subj)
        cursor.execute(f'SELECT id_Преподавателя FROM teacher WHERE class = {cl[0]}')
        teacher_id = cursor.fetchone()[0]
        cursor.execute(f'SELECT ФИО FROM teacher WHERE id_Преподавателя = {teacher_id}')
        teacher = cursor.fetchone()[0]
        day1.append(teacher)
        cursor.execute(f'SELECT type FROM lesson_type WHERE id_type = {subject_type}')
        subject_type_name = cursor.fetchone()[0]
        day1.append(subject_type_name)
        day1.append(cl[2])
        timetable[cl[2] - 1] = day1
        print(timetable)
    return timetable


def get_day_formatting(week, day):
    timetable = get_day(week, day)
    s = f'    {weekday[day - 1]}    \n'
    for cur_day in range(1, 6):
        if timetable[cur_day - 1] == 0:
            s += f'———————————————————\n{cur_day}. Пара отсутствует\n'
        else:
            s += f'———————————————————\n{cur_day}. {timetable[cur_day - 1][0]}\n{timetable[cur_day - 1][1]}\n' \
                 f'{timetable[cur_day - 1][3]}\n' \
                 f'{timetable[cur_day - 1][2]} | {timetable[cur_day - 1][4]}\n'
    return s


def get_week_formatting(week):
    s = ''
    for day in range(1, 7):
        s += get_day_formatting(week, day) + '\n'
    return s

