from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def generate(self, data):
        company_with_qty_the_priduct = super().create_object_company(data)
        formatted_products = [
            f"- {company}: {qty}\n"
            for company, qty in company_with_qty_the_priduct.items()
        ]

        simple_report = super().generate(data)
        complete_report = "".join(formatted_products)

        result = f"""{simple_report}\nProdutos estocados por empresa:\n{
        complete_report}"""

        return result
