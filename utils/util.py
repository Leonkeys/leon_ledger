import datetime


def get_current_date():
    current_year = str(datetime.date.year)
    current_month = str(datetime.date.month)
    if len(current_month) < 2:
        return current_year + "0" + current_month
    return current_year + current_month


def read_file_by_line(file_path):
    with open(file_path, "r") as file_obj:
        for i in file_obj:
            yield i.strip()
