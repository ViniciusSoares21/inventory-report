from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product1 = Product(
        1, "site", "Vjcompany", "2023-04-04", "2025-04-04", "0001", "Git Hub"
    )

    product_result = str(product1)

    string_return = """O produto site fabricado em 2023-04-04 por Vjcompany \
com validade até 2025-04-04 precisa ser armazenado Git Hub."""

    assert string_return == product_result
