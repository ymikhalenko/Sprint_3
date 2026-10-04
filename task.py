import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    @staticmethod
    def __sum_prices_with_discount(total):
        if len(total) > 10:
            return sum(total) * 0.9
        else:
            return sum(total)

    def check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price.get(item))
        return self.__sum_prices_with_discount(total)

    def __some_percent_tax_calculation(self, percent):
        if percent < 0:
            raise ValueError("Tax percent connot be negative")
        total = []
        some_percent_tax = []
        for item in self.__name_items:
            if self.__tax_rate.get(item) == percent:
                some_percent_tax.append(item)
                total.append(self.__item_price.get(item))
        return self.__sum_prices_with_discount(total) * (percent / 100)

    def twenty_percent_tax_calculation(self):
        return self.__some_percent_tax_calculation(20)

    def ten_percent_tax_calculation(self):
        return self.__some_percent_tax_calculation(10)

    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        elif len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return f"+7{telephone_number}"

    @staticmethod
    def get_date_and_time():
        date_and_time = []
        date = [
            [
                "часы",
                lambda x:x.hour
            ],
            [
                "минуты",
                lambda x:x.minute
            ],
            [
                "день",
                lambda x:x.day
            ],
            [
                "месяц",
                lambda x:x.month
            ],
            [
                "год",
                lambda x:x.year
            ]
        ]
        now = datetime.datetime.now()
        for period in date:
            date_and_time.append(f"{period[0]}: {period[1](now)}")
        return date_and_time