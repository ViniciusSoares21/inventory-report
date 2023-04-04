import datetime


def create_object_company(data: list[dict]) -> dict:
    company_product = dict()
    for values in data:
        for chave in values:
            if chave == 'nome_da_empresa':
                if values[chave] in company_product:
                    company_product[values[chave]] += 1
                else:
                    company_product[values[chave]] = 1
    return company_product


def company_more_product(data: list[dict]) -> str:
    company_product = create_object_company(data)
    company_more_product = ''
    more_qty_the_product = max(company_product.values())
    for company, qty in company_product.items():
        if qty == more_qty_the_product:
            company_more_product = company

    return company_more_product


def date_now():
    data = datetime.date.today()
    return f'{data.year}-{data.month}-{data.day}'


def verify_date_more_old(data: list[dict]) -> str:
    date_more_old = date_now()
    for values in data:
        for chave in values:
            if chave == 'data_de_fabricacao':
                d = datetime.datetime.strptime(values[chave], "%Y-%m-%d")
                if d < datetime.datetime.strptime(date_more_old, "%Y-%m-%d"):
                    date_more_old = values[chave]
    return date_more_old


def verify_date_more_new(data: list[dict]) -> str:
    date = datetime.datetime.strptime(date_now(), "%Y-%m-%d")
    filter_date_not_expired = [
        product for product in data
        if datetime.datetime.strptime(product["data_de_validade"],
                                      "%Y-%m-%d") > date
    ]

    date_more_new = '1000-01-01'
    for values in filter_date_not_expired:
        for chave in values:
            if chave == 'data_de_validade':
                d = datetime.datetime.strptime(values[chave], "%Y-%m-%d")
                if abs(d - date) < abs(date - datetime.datetime.strptime(
                        date_more_new, "%Y-%m-%d")):
                    date_more_new = values[chave]
    return date_more_new


class SimpleReport:
    @staticmethod
    def generate(data: list[dict]) -> str:
        company = company_more_product(data)
        date_more_old = verify_date_more_old(data)
        date_more_new = verify_date_more_new(data)

        return (f"Data de fabricação mais antiga: {date_more_old}\n"
                f"Data de validade mais próxima: {date_more_new}\n"
                f"Empresa com mais produtos: {company}"
                )
