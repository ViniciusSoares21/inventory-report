import datetime


class SimpleReport:
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

    def company_more_product(self, data: list[dict]) -> str:
        company_product = self.create_object_company(data)
        return max(company_product, key=company_product.get)

    def date_now():
        data = datetime.date.today()
        return f'{data.year}-{data.month}-{data.day}'

    def verify_date_more_old(self, data: list[dict]) -> str:
        date_more_old = self.date_now()
        for values in data:
            for chave in values:
                if chave == 'data_de_fabricacao':
                    d = datetime.datetime.strptime(values[chave], "%Y-%m-%d")
                    if d < datetime.datetime.strptime(
                            date_more_old, "%Y-%m-%d"):
                        date_more_old = values[chave]
        return date_more_old

    def verify_date_more_new(self, data: list[dict]) -> str:
        date = datetime.datetime.strptime(self.date_now(), "%Y-%m-%d")
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

    @classmethod
    def generate(self, data: list[dict]) -> str:

        company = self.company_more_product(self, data)
        date_more_old = self.verify_date_more_old(self, data)
        date_more_new = self.verify_date_more_new(self, data)

        return (f"Data de fabricação mais antiga: {date_more_old}\n"
                f"Data de validade mais próxima: {date_more_new}\n"
                f"Empresa com mais produtos: {company}"
                )
