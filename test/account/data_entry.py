from datetime import datetime


def get_date(prompt, allow_default=False):
    date_format = "%Y-%m-%d"
    input_date = input(prompt)

    if allow_default and not input_date:
        return datetime.today().strftime(date_format)

    try:
        valid_date = datetime.strptime(input_date, date_format)
        return valid_date.strftime(date_format)
    except:
        print("날짜 형식이 잘못되었습니다. 2000-01-23 과 같은 형식으로 입력하시오")
        return get_date(prompt, allow_default)


def get_amount():
    try:
        amount = int(input("금액을 입력하시오: "))

        if amount <= 0:
            raise ValueError("금액은 0보다 큰 값이어야 합니다.")

        return amount
    except ValueError as e:
        print(e)
        return get_amount()
    except Exception as e:
        print(e)
        return get_amount()


def get_category():
    pass


def get_description():
    pass
