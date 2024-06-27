from datetime import datetime, date, timedelta


def get_birthdays_per_week(users):

    result = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
    today = date.today()
    
    start_of_next_week = today + timedelta(days=(7 - today.weekday()))
    end_of_next_week = start_of_next_week + timedelta(days=4)
    
    for user in users:
        birthday = user['birthday']
        this_year_birthday = birthday.replace(year=today.year)
        birthday_weekday = this_year_birthday.weekday()
        weekday_name = this_year_birthday.strftime('%A')

        if this_year_birthday < today:
            this_year_birthday = birthday.replace(year=today.year + 1)

        if this_year_birthday < end_of_next_week:
            if birthday_weekday < 5:
                result[weekday_name].append(user['name'])
            elif birthday_weekday >= 5:
                result['Monday'].append(user['name'])

    list_k = []

    for key, value in result.items():
        if len(value) == 0:
            list_k.append(key)

    for i in list_k:
        result.pop(i)

    return result


if __name__ == "__main__":

    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")






