# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
def data_is_valid(data):
    dd, mm, yyyy = (data.split('.'))
    dd_, mm_, yyyy_ = int(dd), int(mm), int(yyyy)
    if yyyy_ >= 1 and yyyy_ <= 9999 and mm_ >= 1 and mm_ <= 12 and (
            (is_leap(yyyy_) and dd_ <= 29) or (not is_leap(yyyy_) and dd_ <= 28)):
        return True
    else:
        return False


def is_leap(year_):
    LEAP_MAIN = 4
    LEAP_EXCLUDE = 100
    LEAP_ADDITION = 400

    if year_ % LEAP_MAIN == 0 and year_ % LEAP_EXCLUDE != 0 or year_ % LEAP_ADDITION == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(data_is_valid('30.02.2000'))
